#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   sep-2023
#
# usage:  implement a Python Lambda layer with a langchain virtual environment
#------------------------------------------------------------------------------
locals {
  layer_slug              = "langchain"
  layer_name              = "layer_${local.layer_slug}"
  layer_source_directory  = "${path.module}/python/${local.layer_name}"
  layer_packaging_script  = "${path.module}/scripts/create_pkg_${local.layer_name}.sh"
  layer_package_folder    = "${local.layer_name}_dst"
  layer_dist_package_name = "${local.layer_name}_dst"
}

###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################
resource "null_resource" "package_layer_langchain" {
  triggers = {
    redeployment = sha1(jsonencode([
      file("${local.layer_source_directory}/requirements.txt"),
      file("${local.layer_packaging_script}")
    ]))
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = local.layer_packaging_script

    environment = {
      PACKAGE_NAME     = local.layer_name
      SOURCE_CODE_PATH = local.layer_source_directory
      PACKAGE_FOLDER   = local.layer_package_folder
      RUNTIME          = var.lambda_python_runtime
    }
  }
}

data "archive_file" "layer_langchain" {
  # see https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file
  source_dir  = "${local.layer_source_directory}/${local.layer_package_folder}/"
  output_path = "${local.layer_source_directory}/${local.layer_dist_package_name}.zip"
  type        = "zip"
  depends_on  = [null_resource.package_layer_langchain]
}

resource "aws_lambda_layer_version" "langchain" {
  filename   = data.archive_file.layer_langchain.output_path
  layer_name = "langchain"
  compatible_runtimes = [
    "python3.10",
    "python3.11"
  ]
}
