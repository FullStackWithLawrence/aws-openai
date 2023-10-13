// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const FunctionCreator = {
  api_url: BACKEND_API_URL + 'default-interview-questions',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Python Function Creator",
  assistant_name: "Francine",
  avatar_url: '/applications/FunctionCreator/Francine.svg',
  background_image_url: '/applications/FunctionCreator/FunctionCreator-bg.svg',
  welcome_message: `Hello, I'm Francine, a Python programmer, and I can help you create a Python function.`,
  example_prompts: [],
  placeholder_text: `give Francine a specification for a Python function`,
};

export default FunctionCreator;
