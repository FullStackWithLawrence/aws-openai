// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const ReviewClassifier = {
  api_url: BACKEND_API_URL + 'default-review-classifier',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Product Review Classifier",
  assistant_name: "Ridley",
  avatar_url: '../public/applications/ReviewClassifier/Ridley.svg',
  background_image_url: '../public/applications/ReviewClassifier/ReviewClassifier-bg.jpg',
  welcome_message: `Hello, I'm Ridley, and I can classify product reviews based on their tone and gesticulation.`,
  example_prompts: [
    'this is the best everlasting gobstopper ever!',
    'this newspaper is only good for wrapping fish',
    'tastes like chicken',
  ],
  placeholder_text: `paste a product review for Ridley...`,
};

export default ReviewClassifier;
