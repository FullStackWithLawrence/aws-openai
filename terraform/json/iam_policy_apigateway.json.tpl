{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Action": [
				"s3:PutObject"
			],
			"Effect": "Allow",
      "Resource": [
				"arn:aws:s3:::${bucket_name}*",
				"arn:aws:s3:::${bucket_name}/*"
			],
			"Sid": "1"
		},
    {
      "Effect": "Allow",
      "Action": [
          "lambda:InvokeFunction"
      ],
      "Resource": "*"
    }
	]
}
