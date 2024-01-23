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
  openai_layer_slug              = "openai"
  openai_layer_name              = "layer_${local.openai_layer_slug}"
  openai_layer_parent_directory  = "${path.module}/python"
  openai_layer_source_directory  = "${local.openai_layer_parent_directory}/${local.openai_layer_name}"
  openai_layer_packaging_script  = "${local.openai_layer_source_directory}/create_container.sh"
  openai_layer_package_folder    = local.openai_layer_slug
  openai_layer_dist_build_path   = "${path.module}/build/"
  openai_layer_dist_package_name = "${local.openai_layer_name}_dst.zip"
}

###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################
resource "null_resource" "package_openai_layer" {
  triggers = {
    redeployment = sha1(jsonencode([
      "${path.module}/lambda_layer.tf",
      file("${local.openai_layer_packaging_script}"),
      file("${local.openai_layer_source_directory}/Dockerfile"),
      file("${local.openai_layer_source_directory}/create_container.sh"),
      file("${local.openai_layer_source_directory}/requirements.txt"),
      fileexists("${local.openai_layer_source_directory}/${local.openai_layer_dist_package_name}") ? filebase64("${local.openai_layer_source_directory}/${local.openai_layer_dist_package_name}") : "default"
    ]))
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = local.openai_layer_packaging_script

    environment = {
      SOURCE_CODE_PATH = local.openai_layer_source_directory
      RUNTIME          = var.lambda_python_runtime
      CONTAINER_NAME   = local.openai_layer_name
      PACKAGE_NAME     = local.openai_layer_dist_package_name
    }
  }
}

resource "aws_lambda_layer_version" "openai" {
  filename                 = "${local.openai_layer_source_directory}/${local.openai_layer_dist_package_name}"
  source_code_hash         = fileexists("${local.openai_layer_source_directory}/${local.openai_layer_dist_package_name}") ? filebase64sha256("${local.openai_layer_source_directory}/${local.openai_layer_dist_package_name}") : null
  layer_name               = local.openai_layer_slug
  compatible_architectures = var.compatible_architectures
  compatible_runtimes      = [var.lambda_python_runtime]
  lifecycle {
    create_before_destroy = true
  }
  depends_on = [
    null_resource.package_openai_layer
  ]
}
