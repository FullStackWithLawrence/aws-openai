// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-tweet-classifier";

const TweetClassifier = {
  sidebar_title: "Tweet Classifier",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Tweet Classifier",
  assistant_name: "Clare",
  avatar_url: "/applications/TweetClassifier/Clare.svg",
  background_image_url: "/applications/TweetClassifier/TweetClassifier-bg.jpg",
  welcome_message: `Hello, I'm Clare, and I classify tweets.`,
  example_prompts: [],
  placeholder_text: `paste a tweet for Clare`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default TweetClassifier;
