{
	"Version": "2012-10-17",
	"Statement": [
    {
      "Effect": "Allow",
      "Action": [
          "lambda:InvokeFunction"
      ],
      "Resource": "*"
    },
		{
			"Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
        ],
			"Effect": "Allow",
      "Resource": ["arn:aws:logs:*:*:*"],
			"Sid": "1"
		}
	]
}
