{
    "Version": "2008-10-17",
    "Id": "aaaa-bbbb-cccc-dddd",
    "Statement": [
        {
            "Sid": "1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "${iam_user_arn}"
            },
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::${bucket_name}/*"
        }
    ]
}
