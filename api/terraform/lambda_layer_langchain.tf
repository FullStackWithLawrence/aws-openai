#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   sep-2023
#
# usage:  implement a Python Lambda layer with a virtual environment
#         that includes the packages required by langchain API and LangChain.
#------------------------------------------------------------------------------
locals {
  langchain_layer_slug              = "langchain"
  langchain_layer_name              = "layer_${local.langchain_layer_slug}"
  langchain_layer_parent_directory  = "${path.module}/python"
  langchain_layer_source_directory  = "${local.langchain_layer_parent_directory}/${local.langchain_layer_name}"
  langchain_layer_packaging_script  = "${local.langchain_layer_source_directory}/create_container.sh"
  langchain_layer_package_folder    = local.langchain_layer_slug
  langchain_layer_dist_build_path   = "${path.module}/build/"
  langchain_layer_dist_package_name = "${local.langchain_layer_name}_dst.zip"
}

###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################
resource "null_resource" "package_langchain_layer" {
  triggers = {
    redeployment = sha1(jsonencode([
      "${path.module}/lambda_layer.tf",
      file("${local.langchain_layer_packaging_script}"),
      file("${local.langchain_layer_source_directory}/Dockerfile"),
      file("${local.langchain_layer_source_directory}/create_container.sh"),
      file("${local.langchain_layer_source_directory}/requirements.txt"),
      fileexists("${local.langchain_layer_source_directory}/${local.langchain_layer_dist_package_name}") ? filebase64("${local.langchain_layer_source_directory}/${local.langchain_layer_dist_package_name}") : null
    ]))
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = local.langchain_layer_packaging_script

    environment = {
      SOURCE_CODE_PATH = local.langchain_layer_source_directory
      RUNTIME          = var.lambda_python_runtime
      CONTAINER_NAME   = local.langchain_layer_name
      PACKAGE_NAME     = local.langchain_layer_dist_package_name
    }
  }
}

resource "aws_lambda_layer_version" "langchain" {
  filename                 = "${local.langchain_layer_source_directory}/${local.langchain_layer_dist_package_name}"
  source_code_hash         = fileexists("${local.langchain_layer_source_directory}/${local.langchain_layer_dist_package_name}") ? filebase64sha256("${local.langchain_layer_source_directory}/${local.langchain_layer_dist_package_name}") : "default"
  layer_name               = local.langchain_layer_slug
  compatible_architectures = var.compatible_architectures
  compatible_runtimes      = [var.lambda_python_runtime]
  lifecycle {
    create_before_destroy = true
  }
  depends_on = [
    null_resource.package_langchain_layer
  ]
}
