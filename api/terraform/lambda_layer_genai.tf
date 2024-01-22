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
  genai_layer_slug              = "genai"
  genai_layer_name              = "layer_${local.genai_layer_slug}"
  genai_layer_parent_directory  = "${path.module}/python"
  genai_layer_source_directory  = "${local.genai_layer_parent_directory}/${local.genai_layer_name}"
  genai_layer_packaging_script  = "${local.genai_layer_source_directory}/create_container.sh"
  genai_layer_package_folder    = local.genai_layer_slug
  genai_layer_dist_build_path   = "${path.module}/build/"
  genai_layer_dist_package_name = "${local.genai_layer_name}_dst.zip"
}

###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################
resource "null_resource" "package_genai_layer" {
  triggers = {
    redeployment = sha1(jsonencode([
      "${path.module}/lambda_layer.tf",
      file("${local.genai_layer_packaging_script}"),
      file("${local.genai_layer_source_directory}/Dockerfile"),
      file("${local.genai_layer_source_directory}/create_container.sh"),
      file("${local.genai_layer_source_directory}/requirements.txt"),
      fileexists("${local.genai_layer_source_directory}/${local.genai_layer_dist_package_name}") ? filebase64("${local.genai_layer_source_directory}/${local.genai_layer_dist_package_name}") : null
    ]))
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = local.genai_layer_packaging_script

    environment = {
      SOURCE_CODE_PATH = local.genai_layer_source_directory
      RUNTIME          = var.lambda_python_runtime
      CONTAINER_NAME   = local.genai_layer_name
      PACKAGE_NAME     = local.genai_layer_dist_package_name
    }
  }
}

resource "aws_lambda_layer_version" "genai" {
  filename                 = "${local.genai_layer_source_directory}/${local.genai_layer_dist_package_name}"
  source_code_hash         = fileexists("${local.genai_layer_source_directory}/${local.genai_layer_dist_package_name}") ? filebase64sha256("${local.genai_layer_source_directory}/${local.genai_layer_dist_package_name}") : null
  layer_name               = local.genai_layer_slug
  compatible_architectures = var.compatible_architectures
  compatible_runtimes      = [var.lambda_python_runtime]
  lifecycle {
    create_before_destroy = true
  }
  depends_on = [
    null_resource.package_genai_layer
  ]
}
