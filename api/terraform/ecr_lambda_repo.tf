#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   sep-2023
#
# usage:  Build a one-size-fits-all ECR repository to hold the
#         Lambda function container image.
#------------------------------------------------------------------------------
locals {
  image_tag = "v1.0.7"
}



resource "null_resource" "build_and_push" {
  triggers = {
      dockerfile    = filesha1("${path.module}/Dockerfile")
      requirements  = filesha1("${path.module}/requirements.txt")
      source_hash   = sha1(join("", [for f in fileset("${path.module}/python/openai_api", "**") : filesha1("${path.module}/python/openai_api/${f}")]))
    }
  provisioner "local-exec" {
    interpreter = ["/bin/bash", "-c"]

    command = <<EOT
set -e

AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=${var.aws_region}
REPO=${aws_ecr_repository.lambda_repo.name}

IMAGE_URI=$AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO:${local.image_tag}

aws ecr get-login-password --region $REGION \
| docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com


docker build --platform linux/amd64 -t $REPO:${local.image_tag} .
docker tag $REPO:${local.image_tag} $IMAGE_URI
docker push $IMAGE_URI

EOT
  }
}

resource "aws_ecr_repository" "lambda_repo" {
  name = "lambda-openai-v2"
}
