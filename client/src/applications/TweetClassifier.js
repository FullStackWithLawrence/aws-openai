// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const TweetClassifier = {
  api_url: BACKEND_API_URL + 'default-tweet-classifier',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Tweet Classifier",
  assistant_name: "Clare",
  avatar_url: '../public/applications/TweetClassifier/Clare.svg',
  background_image_url: '../public/applications/TweetClassifier/TweetClassifier-bg.jpg',
  welcome_message: `Hello, I'm Clare, and I classify tweets.`,
  example_prompts: [],
  placeholder_text: `paste a tweet for Clare`,
};

export default TweetClassifier;
