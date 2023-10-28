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
  layer_source_directory  = "${path.module}/python/${local.layer_name}"
  layer_packaging_script  = "${local.layer_source_directory}/create_pkg.sh"
  layer_package_folder    = local.layer_slug
  layer_dist_package_name = "${local.layer_name}_dst"
}

###############################################################################
# Python package
# https://alek-cora-glez.medium.com/deploying-aws-lambda-function-with-terraform-custom-dependencies-7874407cd4fc
###############################################################################
resource "null_resource" "package_layer_genai" {
  triggers = {
    redeployment = sha1(jsonencode([
      "${path.module}/lambda_layer.tf",
      file("${local.layer_source_directory}/requirements.txt"),
      file("${local.layer_packaging_script}"),
      file("${local.layer_source_directory}/openai_utils/__init__.py"),
      file("${local.layer_source_directory}/openai_utils/const.py"),
      file("${local.layer_source_directory}/openai_utils/utils.py"),
      file("${local.layer_source_directory}/openai_utils/validators.py"),
    ]))
  }

  provisioner "local-exec" {
    interpreter = ["/bin/bash"]
    command     = local.layer_packaging_script

    environment = {
      LAYER_NAME       = local.layer_slug
      SOURCE_CODE_PATH = local.layer_source_directory
      PACKAGE_FOLDER   = local.layer_package_folder
      RUNTIME          = var.lambda_python_runtime
    }
  }
}

data "archive_file" "layer_genai" {
  # see https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file
  source_dir  = "${local.layer_source_directory}/${local.layer_package_folder}/"
  output_path = "${local.layer_source_directory}/${local.layer_dist_package_name}.zip"
  type        = "zip"
  depends_on  = [null_resource.package_layer_genai]
}

resource "aws_lambda_layer_version" "genai" {
  filename = data.archive_file.layer_genai.output_path
  #  source_code_hash         = filebase64sha256(data.archive_file.layer_genai.output_path)
  layer_name               = local.layer_slug
  compatible_architectures = ["x86_64", "arm64"]
  compatible_runtimes      = [var.lambda_python_runtime]
}
