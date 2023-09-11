#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:       sep-2023
#
# usage:      local variable declaration and common infrastructure for the service
#------------------------------------------------------------------------------
locals {
  collection_id = "${var.shared_resource_identifier}-collection"
  table_name    = var.shared_resource_identifier
}
