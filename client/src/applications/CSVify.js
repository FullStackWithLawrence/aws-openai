// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const CSVify = {
  api_url: BACKEND_API_URL + 'default-parse-data',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "CSVify",
  assistant_name: "Chad",
  avatar_url: '../public/applications/CSVify/Chad.svg',
  background_image_url: '../public/applications/CSVify/CSVify-bg.jpg',
  welcome_message: `Hello, I'm Chad, and I convert unstructured text data to CSV. Paste some text into the chat box to get started.`,
  example_prompts: [],
  placeholder_text: `send some data to Chad`,
};

export default CSVify;
