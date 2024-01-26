# -*- coding: utf-8 -*-
"""A utility class for introspecting AWS infrastructure."""

import json

# python stuff
import os
import socket

# our stuff
from openai_api.common.conf import Services, settings
from openai_api.common.utils import recursive_sort_dict


# pylint: disable=too-many-public-methods
class AWSInfrastructureConfig:
    """AWS Infrastructure Config"""

    _domain = None

    @property
    def dump(self):
        """Return a dict of the AWS infrastructure config."""
        retval = {}
        if Services.enabled(Services.AWS_APIGATEWAY):
            api = self.get_api(settings.aws_apigateway_name)
            retval["apigateway"] = {
                "api_id": api.get("id"),
                "stage": self.get_api_stage(),
                "domains": self.get_api_custom_domains(),
            }
        if Services.enabled(Services.AWS_S3):
            retval["s3"] = {"bucket_name": self.get_bucket_by_prefix(settings.aws_s3_bucket_name)}
        if Services.enabled(Services.AWS_DYNAMODB):
            retval["dynamodb"] = {"table_name": self.get_dyanmodb_table_by_name(settings.aws_dynamodb_table_id)}
        if Services.enabled(Services.AWS_REKOGNITION):
            retval["rekognition"] = {
                "collection_id": self.get_rekognition_collection_by_id(settings.aws_rekognition_collection_id)
            }
        if Services.enabled(Services.AWS_IAM):
            retval["iam"] = {"policies": self.get_iam_policies(), "roles": self.get_iam_roles()}
        if Services.enabled(Services.AWS_LAMBDA):
            retval["lambda"] = self.get_lambdas()
        if Services.enabled(Services.AWS_ROUTE53):
            retval["route53"] = self.get_dns_record_from_hosted_zone()
        return recursive_sort_dict(retval)

    def get_lambdas(self):
        """Return a dict of the AWS Lambdas."""
        lambda_client = settings.aws_session.client("lambda")
        lambdas = lambda_client.list_functions()["Functions"]
        retval = {
            lambda_function["FunctionName"]: lambda_function["FunctionArn"]
            for lambda_function in lambdas
            if settings.shared_resource_identifier in lambda_function["FunctionName"]
        }
        return retval or {}

    def get_iam_policies(self):
        """Return a dict of the AWS IAM policies."""
        iam_client = settings.aws_session.client("iam")
        policies = iam_client.list_policies()["Policies"]
        retval = {}
        for policy in policies:
            if settings.shared_resource_identifier in policy["PolicyName"]:
                policy_version = iam_client.get_policy(PolicyArn=policy["Arn"])["Policy"]["DefaultVersionId"]
                policy_document = iam_client.get_policy_version(PolicyArn=policy["Arn"], VersionId=policy_version)[
                    "PolicyVersion"
                ]["Document"]
                retval[policy["PolicyName"]] = {"Arn": policy["Arn"], "Policy": policy_document}
        return retval

    def get_iam_roles(self):
        """Return a dict of the AWS IAM roles."""
        iam_client = settings.aws_session.client("iam")
        roles = iam_client.list_roles()["Roles"]
        retval = {}
        for role in roles:
            if settings.shared_resource_identifier in role["RoleName"]:
                attached_policies = iam_client.list_attached_role_policies(RoleName=role["RoleName"])[
                    "AttachedPolicies"
                ]
                retval[role["RoleName"]] = {
                    "Arn": role["Arn"],
                    "Role": role,
                    "AttachedPolicies": attached_policies,
                }
        return retval or {}

    def get_api_stage(self) -> str:
        """Return the API stage."""
        api = self.get_api(settings.aws_apigateway_name) or {}
        api_id = api.get("id")
        if api_id:
            response = settings.aws_apigateway_client.get_stages(restApiId=api_id)
            # Assuming you want the most recently deployed stage
            stages = response.get("item", [])
            if stages:
                retval = stages[-1]["stageName"]
                return retval
        return ""

    def get_api_custom_domains(self) -> list:
        """Return the API custom domains."""

        def filter_dicts(lst):
            return [d for d in lst if "domainName" in d and settings.shared_resource_identifier in d["domainName"]]

        response = settings.aws_apigateway_client.get_domain_names()
        retval = response.get("items", [])
        return filter_dicts(retval)

    def get_url(self, path) -> str:
        """Return the url for the given path."""
        if settings.aws_apigateway_create_custom_domaim:
            return f"https://{settings.aws_apigateway_domain_name}{path}"
        return f"https://{settings.aws_apigateway_domain_name}/{self.get_api_stage()}{path}"

    def aws_connection_works(self):
        """Test that the AWS connection works."""
        try:
            # pylint: disable=pointless-statement
            settings.aws_session.region_name
            return True
        except Exception:  # pylint: disable=broad-exception-caught
            return False

    @property
    def domain(self):
        """Return the domain."""
        if not self._domain:
            if settings.aws_apigateway_create_custom_domaim:
                self._domain = (
                    os.getenv(key="DOMAIN")
                    or "api." + settings.shared_resource_identifier + "." + settings.aws_apigateway_root_domain
                )
                return self._domain

            response = settings.aws_apigateway_client.get_rest_apis()
            for item in response["items"]:
                if item["name"] == self.api_gateway_name:
                    api_id = item["id"]
                    self._domain = f"{api_id}.execute-api.{settings.aws_region}.amazonaws.com"
        return self._domain

    @property
    def api_gateway_name(self):
        """Return the API Gateway name."""
        return settings.shared_resource_identifier + "-api"

    def domain_exists(self) -> bool:
        """Test that the domain exists."""
        try:
            socket.gethostbyname(settings.aws_apigateway_domain_name)
            return True
        except socket.gaierror:
            return False

    def get_bucket_by_prefix(self, bucket_prefix) -> str:
        """Return the bucket name given the bucket prefix."""
        try:
            for bucket in settings.aws_s3_client.list_buckets()["Buckets"]:
                if bucket["Name"].startswith(bucket_prefix):
                    return f"arn:aws:s3:::{bucket['Name']}"
        except TypeError:
            # TypeError: startswith first arg must be str or a tuple of str, not NoneType
            pass
        return None

    def bucket_exists(self, bucket_prefix) -> bool:
        """Test that the S3 bucket exists."""
        bucket = self.get_bucket_by_prefix(bucket_prefix)
        return bucket is not None

    def get_dyanmodb_table_by_name(self, table_name) -> str:
        """Return the DynamoDB table given the table name."""
        response = settings.aws_dynamodb_client.list_tables()
        for table in response["TableNames"]:
            if table == table_name:
                table_description = settings.aws_dynamodb_client.describe_table(TableName=table_name)
                return table_description["Table"]["TableArn"]
        return None

    def dynamodb_table_exists(self, table_name) -> bool:
        """Test that the DynamoDB table exists."""
        table = self.get_dyanmodb_table_by_name(table_name)
        return table is not None

    def api_exists(self, api_name: str) -> bool:
        """Test that the API Gateway exists."""
        response = settings.aws_apigateway_client.get_rest_apis()

        for item in response["items"]:
            if item["name"] == api_name:
                return True
        return False

    def get_api(self, api_name: str) -> dict:
        """Test that the API Gateway exists."""
        response = settings.aws_apigateway_client.get_rest_apis()

        for item in response["items"]:
            if item["name"] == api_name:
                return item
        return {}

    def api_resource_and_method_exists(self, path, method) -> bool:
        """Test that the API Gateway resource and method exists."""
        api = self.get_api(settings.aws_apigateway_name) or {}
        api_id = api.get("id")
        resources = settings.aws_apigateway_client.get_resources(restApiId=api_id)
        for resource in resources["items"]:
            if resource["path"] == path:
                try:
                    settings.aws_apigateway_client.get_method(
                        restApiId=api_id, resourceId=resource["id"], httpMethod=method
                    )
                    return True
                except settings.aws_apigateway_client.exceptions.NotFoundException:
                    return False

        return False

    def get_api_keys(self) -> str:
        """Test that the API Gateway exists."""
        response = settings.aws_apigateway_client.get_api_keys(includeValues=True)
        for item in response["items"]:
            if item["name"] == settings.shared_resource_identifier:
                return item["value"]
        return False

    def get_rekognition_collection_by_id(self, collection_id) -> str:
        """Return the Rekognition collection."""
        response = settings.aws_rekognition_client.list_collections()
        for collection in response["CollectionIds"]:
            if collection == collection_id:
                return collection
        return None

    def rekognition_collection_exists(self) -> bool:
        """Test that the Rekognition collection exists."""
        collection = self.get_rekognition_collection_by_id(settings.aws_rekognition_collection_id)
        return collection is not None

    def get_hosted_zone(self, domain_name) -> str:
        """Return the hosted zone."""
        response = settings.aws_route53_client.list_hosted_zones()
        for hosted_zone in response["HostedZones"]:
            if hosted_zone["Name"] == domain_name or hosted_zone["Name"] == f"{domain_name}.":
                return hosted_zone["Id"]
        return None

    def get_dns_record_from_hosted_zone(self) -> str:
        """Return the DNS record from the hosted zone."""
        hosted_zone_id = self.get_hosted_zone(settings.aws_apigateway_root_domain)
        if hosted_zone_id:
            response = settings.aws_route53_client.list_resource_record_sets(HostedZoneId=hosted_zone_id)
            for record in response["ResourceRecordSets"]:
                if (
                    record["Name"] == settings.aws_apigateway_domain_name
                    or record["Name"] == f"{settings.aws_apigateway_domain_name}."
                ):
                    return record
        return None


class SingletonConfig:
    """Singleton for Settings"""

    _instance = None

    def __new__(cls):
        """Create a new instance of Settings"""
        if cls._instance is None:
            cls._instance = super(SingletonConfig, cls).__new__(cls)
            cls._instance._config = AWSInfrastructureConfig()
        return cls._instance

    @property
    def config(self) -> AWSInfrastructureConfig:
        """Return the settings"""
        return self._config  # pylint: disable=E1101


aws_infrastructure_config = SingletonConfig().config
