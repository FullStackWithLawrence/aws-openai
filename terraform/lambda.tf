locals {
  lambda_role_name   = "${var.shared_resource_identifier}-lambda"
  lambda_policy_name = "${var.shared_resource_identifier}-lambda"
}

resource "aws_iam_role" "lambda" {
  name               = local.lambda_role_name
  assume_role_policy = file("${path.module}/json/iam_role_lambda.json")
  tags               = var.tags
}

data "template_file" "iam_policy_lambda" {
  template = file("${path.module}/json/iam_policy_lambda.json")
  vars     = {}
}
resource "aws_iam_policy" "lambda" {
  name        = local.lambda_policy_name
  description = "generic IAM policy"
  policy      = data.template_file.iam_policy_lambda.rendered
}


resource "aws_iam_role_policy_attachment" "lambda" {
  role       = aws_iam_role.lambda.id
  policy_arn = aws_iam_policy.lambda.arn
}

# ----------------------------------------------------------------------
# FIX NOTE: these permissions are too broad.
# ----------------------------------------------------------------------
resource "aws_iam_role_policy_attachment" "lambda_CloudWatchFullAccess" {
  role       = aws_iam_role.lambda.id
  policy_arn = "arn:aws:iam::aws:policy/CloudWatchFullAccess"
}
