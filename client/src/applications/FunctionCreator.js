// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-function-from-spec";

const FunctionCreator = {
  sidebar_title: "Python Function Creator",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Python Function Creator",
  assistant_name: "Francine",
  avatar_url: "/applications/FunctionCreator/Francine.svg",
  background_image_url: "/applications/FunctionCreator/FunctionCreator-bg.svg",
  welcome_message: `Hello, I'm Francine, a Python programmer, and I can help you create a Python function.`,
  example_prompts: [],
  placeholder_text: `give Francine a specification for a Python function`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default FunctionCreator;
