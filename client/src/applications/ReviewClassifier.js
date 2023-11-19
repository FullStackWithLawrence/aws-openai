// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-review-classifier";

const ReviewClassifier = {
  sidebar_title: "Product Review Classifier",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Product Review Classifier",
  assistant_name: "Ridley",
  avatar_url: "/applications/ReviewClassifier/Ridley.svg",
  background_image_url:
    "/applications/ReviewClassifier/ReviewClassifier-bg.jpg",
  welcome_message: `Hello, I'm Ridley, and I can classify product reviews based on their tone and gesticulation.`,
  example_prompts: [
    "this is the best everlasting gobstopper ever!",
    "this newspaper is only good for wrapping fish",
    "tastes like chicken",
  ],
  placeholder_text: `paste a product review for Ridley...`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default ReviewClassifier;
