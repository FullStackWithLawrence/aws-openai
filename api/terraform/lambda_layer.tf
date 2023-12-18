#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   sep-2023
#
# usage:  implement a Python Lambda layer with a virtual environment
#         that includes the packages required by OpenAI API and LangChain.
#------------------------------------------------------------------------------
locals {
  layer_slug              = "genai"
  layer_name              = "layer_${local.layer_slug}"
  layer_parent_directory  = "${path.module}/python/"
  layer_source_directory  = "${local.layer_parent_directory}${local.layer_name}"
  layer_packaging_script  = "${local.layer_source_directory}/create_container.sh"
  layer_package_folder    = local.layer_slug
  layer_dist_build_path   = "${path.module}/build/"
  layer_dist_package_name = "${local.layer_dist_build_path}${local.layer_name}_dst.zip"
}

###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################
resource "null_resource" "package_layer_genai" {
  triggers = {
    redeployment = sha1(jsonencode([
      "${path.module}/lambda_layer.tf",
      file("${local.layer_packaging_script}"),
      file("${local.layer_source_directory}/Dockerfile"),
      file("${local.layer_source_directory}/create_container.sh"),
      file("${local.layer_source_directory}/requirements.txt"),
      fileexists("${local.layer_source_directory}/${local.layer_dist_package_name}") ? filebase64("${local.layer_source_directory}/${local.layer_dist_package_name}") : null
    ]))
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = local.layer_packaging_script

    environment = {
      PARENT_DIRECTORY = local.layer_parent_directory
      SOURCE_CODE_PATH = local.layer_source_directory
      RUNTIME          = var.lambda_python_runtime
      CONTAINER_NAME   = local.layer_name
      PACKAGE_NAME     = local.layer_dist_package_name
    }
  }
}

resource "aws_lambda_layer_version" "genai" {
  filename                 = "${local.layer_source_directory}/${local.layer_dist_package_name}"
  source_code_hash         = fileexists("${local.layer_source_directory}/${local.layer_dist_package_name}") ? filebase64sha256("${local.layer_source_directory}/${local.layer_dist_package_name}") : null
  layer_name               = local.layer_slug
  compatible_architectures = var.compatible_architectures
  compatible_runtimes      = [var.lambda_python_runtime]
  lifecycle {
    create_before_destroy = true
  }
  depends_on = [
    null_resource.package_layer_genai
  ]
}
