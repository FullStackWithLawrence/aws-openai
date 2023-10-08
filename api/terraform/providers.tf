#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:       sep-2023
#
# usage:      all Terraform providers
#------------------------------------------------------------------------------
provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}
