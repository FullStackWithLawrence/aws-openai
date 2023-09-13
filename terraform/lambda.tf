#------------------------------------------------------------------------------
# written by: Lawrence McDaniel
#             https://lawrencemcdaniel.com/
#
# date:   sep-2023
#
# usage:  configure common Lambda IAM role and policy to enable
#         logging to Cloudwatch.
#------------------------------------------------------------------------------
locals {
  lambda_role_name   = "${var.shared_resource_identifier}-lambda"
  lambda_policy_name = "${var.shared_resource_identifier}-lambda"
}

resource "aws_iam_role" "lambda" {
  name               = local.lambda_role_name
  assume_role_policy = file("${path.module}/json/iam_role_lambda.json")
  tags               = var.tags
}

resource "aws_iam_role_policy_attachment" "lambda_CloudWatchFullAccess" {
  role       = aws_iam_role.lambda.id
  policy_arn = "arn:aws:iam::aws:policy/CloudWatchFullAccess"
}

resource "aws_iam_role_policy" "iam_policy_lambda" {
  name   = local.iam_role_policy_name
  role   = aws_iam_role.lambda.id
  policy = file("${path.module}/json/iam_policy_lambda.json")
}
