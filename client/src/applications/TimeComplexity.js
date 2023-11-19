// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-time-complexity";

const TimeComplexity = {
  sidebar_title: "TimeComplexity",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "TimeComplexity",
  assistant_name: "Christine",
  avatar_url: "/applications/TimeComplexity/Christine.svg",
  background_image_url: "/applications/TimeComplexity/TimeComplexity-bg.svg",
  welcome_message: `Hello, I'm Christine, and I calculate the time complexity of Python code.`,
  example_prompts: [],
  placeholder_text: `upload a Python file`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: true,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default TimeComplexity;
