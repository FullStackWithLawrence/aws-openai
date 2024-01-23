#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   sep-2023
#
# usage:  implement a Python Lambda layer containing Pandas and NumPy.
#------------------------------------------------------------------------------
locals {
  pandas_layer_slug              = "pandas"
  pandas_layer_name              = "layer_${local.pandas_layer_slug}"
  pandas_layer_parent_directory  = "${path.module}/python"
  pandas_layer_source_directory  = "${local.pandas_layer_parent_directory}/${local.pandas_layer_name}"
  pandas_layer_packaging_script  = "${local.pandas_layer_source_directory}/create_container.sh"
  pandas_layer_package_folder    = local.pandas_layer_slug
  pandas_layer_dist_build_path   = "${path.module}/build/"
  pandas_layer_dist_package_name = "${local.pandas_layer_name}_dst.zip"
}

###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################
resource "null_resource" "package_pandas_layer" {
  triggers = {
    redeployment = sha1(jsonencode([
      "${path.module}/lambda_layer.tf",
      file("${local.pandas_layer_packaging_script}"),
      file("${local.pandas_layer_source_directory}/Dockerfile"),
      file("${local.pandas_layer_source_directory}/create_container.sh"),
      file("${local.pandas_layer_source_directory}/requirements.txt"),
      fileexists("${local.pandas_layer_source_directory}/${local.pandas_layer_dist_package_name}") ? filebase64("${local.pandas_layer_source_directory}/${local.pandas_layer_dist_package_name}") : "default"
    ]))
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = local.pandas_layer_packaging_script

    environment = {
      SOURCE_CODE_PATH = local.pandas_layer_source_directory
      RUNTIME          = var.lambda_python_runtime
      CONTAINER_NAME   = local.pandas_layer_name
      PACKAGE_NAME     = local.pandas_layer_dist_package_name
    }
  }
}

resource "aws_lambda_layer_version" "pandas" {
  filename                 = "${local.pandas_layer_source_directory}/${local.pandas_layer_dist_package_name}"
  source_code_hash         = fileexists("${local.pandas_layer_source_directory}/${local.pandas_layer_dist_package_name}") ? filebase64sha256("${local.pandas_layer_source_directory}/${local.pandas_layer_dist_package_name}") : null
  layer_name               = local.pandas_layer_slug
  compatible_architectures = var.compatible_architectures
  compatible_runtimes      = [var.lambda_python_runtime]
  lifecycle {
    create_before_destroy = true
  }
  depends_on = [
    null_resource.package_pandas_layer
  ]
}
