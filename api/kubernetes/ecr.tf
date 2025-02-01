#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   feb-2024
#
# usage:  build and upload a Docker image to AWS Elastic Container Registry (ECR)
#------------------------------------------------------------------------------
locals {
  ecr_repo             = "chat_api"
  ecr_source_directory = "${path.module}../python/openai_api/"

  ecr_build_path   = "${path.module}/ecr_build"
  ecr_build_script = "${local.ecr_build_path}/build.sh"
}

resource "aws_ecr_repository" "chat_api" {
  name                 = local.ecr_repo
  image_tag_mutability = "IMMUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
  tags = var.tags

}

###############################################################################
# Python package
###############################################################################
resource "null_resource" "chat_api" {
  triggers = {
    always_redeploy = timestamp()
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = local.ecr_build_script

    environment = {
      BUILD_PATH     = local.ecr_build_path
      CONTAINER_NAME = local.ecr_repo
      AWS_REGION     = var.aws_region
      AWS_ACCOUNT_ID = var.aws_account_id
    }
  }

  depends_on = [aws_ecr_repository.chat_api]
}
