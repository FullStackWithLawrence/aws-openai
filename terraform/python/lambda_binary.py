# ------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:       sep-2023
#
# Rekognition.search_faces_by_image()
# ------------------------------------
# For a given input image, first detects the largest face in the image,
# and then searches the specified collection for matching faces.
# The operation compares the features of the input face with faces in the specified collection.
#
# The response returns an array of faces that match, ordered by similarity
# score with the highest similarity first. More specifically, it is an
# array of metadata for each face match found. Along with the metadata,
# the response also includes a similarity indicating how similar the face
# is to the input face. In the response, the operation also returns the
# bounding box (and a confidence level that the bounding box contains a face)
# of the face that Amazon Rekognition used for the input image.
#
# Notes:
# - incoming image file is base64 encoded.
#   see https://code.tutsplus.com/base64-encoding-and-decoding-using-python--cms-25588t
#
# - The image must be either a PNG or JPEG formatted file.
#
# OFFICIAL DOCUMENTATION:
# - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/search_faces_by_image.html
# - https://docs.aws.amazon.com/rekognition_client/latest/dg/example_rekognition_Usage_FindFacesInCollection_section.html
#
# GISTS:
# - https://gist.github.com/alexcasalboni/0f21a1889f09760f8981b643326730ff
# ------------------------------------------------------------------------------
import sys, traceback  # libraries for error management
import os  # library for interacting with the operating system
import platform  # library to view informatoin about the server host this Lambda runs on
import json  # library for interacting with JSON data https://www.json.org/json-en.html
import base64  # library with base63 encoding/decoding functions
import boto3  # AWS SDK for Python https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
import openai

MAX_FACES = int(os.environ["MAX_FACES_COUNT"])
THRESHOLD = float(os.environ["FACE_DETECT_THRESHOLD"])
QUALITY_FILTER = os.environ["QUALITY_FILTER"]
TABLE_ID = os.environ["TABLE_ID"]
AWS_REGION = os.environ["REGION"]
COLLECTION_ID = os.environ["COLLECTION_ID"]
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() in ("true", "1", "t")

rekognition_client = boto3.client("rekognition", AWS_REGION)

dynamodb_client = boto3.resource("dynamodb")
dynamodb_table = dynamodb_client.Table(TABLE_ID)


def handler(event, context):
    """
    Facial recognition image analysis and search for indexed faces. invoked by API Gateway.
    """
    if DEBUG_MODE:
        cloudwatch_dump = {
            "environment": {
                "os": os.name,
                "system": platform.system(),
                "release": platform.release(),
                "boto3": boto3.__version__,
                "openai": openai.__version__,
                "MAX_FACES": MAX_FACES,
                "THRESHOLD": THRESHOLD,
                "QUALITY_FILTER": QUALITY_FILTER,
                "TABLE_ID": TABLE_ID,
                "AWS_REGION": AWS_REGION,
                "COLLECTION_ID": COLLECTION_ID,
                "DEBUG_MODE": DEBUG_MODE,
            }
        }
        print(json.dumps(cloudwatch_dump))
        print(json.dumps({"event": event}))

    def http_response_factory(status_code: int, body: json) -> json:
        """
        Generate a standardized JSON return dictionary for all possible response scenarios.

        status_code: an HTTP response code. see https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        body: a JSON dict of Rekognition results for status 200, an error dict otherwise.

        see https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html
        """
        if status_code < 100 or status_code > 599:
            raise ValueError(
                "Invalid HTTP response code received: {status_code}".format(
                    status_code=status_code
                )
            )

        if DEBUG_MODE:
            retval = {
                "isBase64Encoded": False,
                "statusCode": status_code,
                "headers": {"Content-Type": "application/json"},
                "body": body,
            }
            # log our output to the CloudWatch log for this Lambda
            print(json.dumps({"retval": retval}))

        # see https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html
        retval = {
            "isBase64Encoded": False,
            "statusCode": status_code,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(body),
        }

        return retval

    def exception_response_factory(exception) -> json:
        """
        Generate a standardized error response dictionary that includes
        the Python exception type and stack trace.

        exception: a descendant of Python Exception class
        """
        exc_info = sys.exc_info()
        retval = {
            "error": str(exception),
            "description": "".join(traceback.format_exception(*exc_info)),
        }

        return retval

    # all good, lets process the event!
    faces = {}  # Rekognition return value
    matched_faces = []  # any indexed faces found in the Rekognition return value
    try:
        # see
        #  - https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
        #  - line 39, in _bytes_from_decode_data ValueError: string argument should contain only ASCII characters
        #  - https://stackoverflow.com/questions/53340627/typeerror-expected-bytes-like-object-not-str
        #  - alternate syntax: image_raw = ''.join(image_raw).encode('ascii').strip()
        image_raw = str(event["body"]).encode("ascii")
        image_decoded = base64.b64decode(image_raw)

        # https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
        # Image: base64-encoded bytes or an S3 object.
        # Image={
        #     'Bytes': b'bytes',
        #     'S3Object': {
        #         'Bucket': 'string',
        #         'Name': 'string',
        #         'Version': 'string'
        #     }
        # },
        image = {"Bytes": image_decoded}

        faces = rekognition_client.search_faces_by_image(
            Image=image,
            CollectionId=COLLECTION_ID,
            MaxFaces=MAX_FACES,
            FaceMatchThreshold=THRESHOLD,
            QualityFilter=QUALITY_FILTER,
        )

        # ----------------------------------------------------------------------
        # return structure: doc/rekogition_search_faces_by_image.json
        # ----------------------------------------------------------------------
        for face in faces["FaceMatches"]:
            item = dynamodb_table.get_item(Key={"FaceId": face["Face"]["FaceId"]})
            if "Item" in item:
                matched = (
                    str(item["Item"]["ExternalImageId"])
                    .replace("-", " ")
                    .replace("_", " ")
                    .replace(".jpg", "")
                    .replace(".png", "")
                    .capitalize()
                )
                matched_faces.append(matched)

    # handle anything that went wrong
    # see https://docs.aws.amazon.com/rekognition/latest/dg/error-handling.html
    except rekognition_client.exceptions.InvalidParameterException as e:
        # If no faces are detected in the image, then index_faces()
        # returns an InvalidParameterException error
        pass

    except (
        rekognition_client.exceptions.ThrottlingException,
        rekognition_client.exceptions.ProvisionedThroughputExceededException,
        rekognition_client.exceptions.ServiceQuotaExceededException,
    ) as e:
        return http_response_factory(
            status_code=401, body=exception_response_factory(e)
        )

    except rekognition_client.exceptions.AccessDeniedException as e:
        return http_response_factory(
            status_code=403, body=exception_response_factory(e)
        )

    except rekognition_client.exceptions.ResourceNotFoundException as e:
        return http_response_factory(
            status_code=404, body=exception_response_factory(e)
        )

    except (
        rekognition_client.exceptions.InvalidS3ObjectException,
        rekognition_client.exceptions.ImageTooLargeException,
        rekognition_client.exceptions.InvalidImageFormatException,
    ) as e:
        return http_response_factory(
            status_code=406, body=exception_response_factory(e)
        )

    except (rekognition_client.exceptions.InternalServerError, Exception) as e:
        return http_response_factory(
            status_code=500, body=exception_response_factory(e)
        )

    # success!! return the results
    retval = {
        "faces": faces,  # all of the faces that Rekognition found in the image
        "matchedFaces": matched_faces,  # any indexed faces found in DynamoDB
    }
    return http_response_factory(status_code=200, body=retval)
