#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date: sep-2023
#
# usage:  implement a custom domain for API Gateway endpoint.
#------------------------------------------------------------------------------
locals {
  api_gateway_subdomain = "api.${var.shared_resource_identifier}.${var.root_domain}"
}

# WARNING: You need a pre-existing Route53 Hosted Zone
# for root_domain located in your AWS account.
# see: https://aws.amazon.com/route53/
data "aws_route53_zone" "root_domain" {
  count = var.create_custom_domain ? 1 : 0
  name  = var.root_domain
}

# see https://registry.terraform.io/providers/-/aws/4.51.0/docs/resources/api_gateway_domain_name
resource "aws_api_gateway_domain_name" "openai" {
  count                    = var.create_custom_domain ? 1 : 0
  domain_name              = local.api_gateway_subdomain
  regional_certificate_arn = module.acm[count.index].acm_certificate_arn
  tags                     = var.tags
  endpoint_configuration {
    types = ["REGIONAL"]
  }

}

# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/api_gateway_base_path_mapping
resource "aws_api_gateway_base_path_mapping" "openai" {
  count       = var.create_custom_domain ? 1 : 0
  api_id      = aws_api_gateway_rest_api.openai.id
  stage_name  = aws_api_gateway_stage.openai.stage_name
  domain_name = aws_api_gateway_domain_name.openai[count.index].domain_name
}
resource "aws_route53_record" "api" {
  count   = var.create_custom_domain ? 1 : 0
  zone_id = data.aws_route53_zone.root_domain[count.index].id
  name    = local.api_gateway_subdomain
  type    = "A"

  alias {
    name                   = aws_api_gateway_domain_name.openai[count.index].regional_domain_name
    zone_id                = aws_api_gateway_domain_name.openai[count.index].regional_zone_id
    evaluate_target_health = false
  }
}

module "acm" {
  count   = var.create_custom_domain ? 1 : 0
  source  = "terraform-aws-modules/acm/aws"
  version = "~> 6.0"

  # un-comment this if you choose a region other than us-east-1
  # providers = {
  #   aws = var.aws_region
  # }

  domain_name       = local.api_gateway_subdomain
  zone_id           = data.aws_route53_zone.root_domain[count.index].id
  validation_method = "DNS"

  subject_alternative_names = [
    "*.${local.api_gateway_subdomain}",
  ]
  tags = var.tags

  wait_for_validation = true
}
