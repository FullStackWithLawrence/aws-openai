
locals {
  s3_bucket_name = "api.${var.shared_resource_identifier}.${var.root_domain}"
}

resource "aws_s3_bucket" "openai" {
  bucket = local.s3_bucket_name
  tags   = var.tags
}

data "aws_iam_policy_document" "s3_bucket_policy" {
  statement {
    actions = [
      "s3:PutObject",
      "s3:GetObject",
      "s3:ListBucket",
      "s3:DeleteObject",
    ]

    principals {
      type        = "AWS"
      identifiers = ["arn:aws:iam::${data.aws_caller_identity.current.account_id}:user/mcdaniel"]
    }

    resources = [
      "${aws_s3_bucket.openai.arn}/*",
      "${aws_s3_bucket.openai.arn}"
    ]
  }
}

resource "aws_s3_bucket_policy" "openai_bucket_policy" {
  bucket = aws_s3_bucket.openai.id
  policy = data.aws_iam_policy_document.s3_bucket_policy.json
}
