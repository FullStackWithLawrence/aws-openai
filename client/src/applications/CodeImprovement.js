// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-code-improvement";

const CodeImprovement = {
  sidebar_title: "Coding CoPilot",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Python Code Evaluator",
  assistant_name: "Camilla",
  avatar_url: "/applications/CodeImprovement/Camilla.svg",
  background_image_url: "/applications/CodeImprovement/CodeImprovement-bg.svg",
  welcome_message: `Hello, I'm Camilla, a Python programmer, and I can help you improve your Python code.`,
  example_prompts: [],
  placeholder_text: `give Camilla a Python code snippet to evaluate`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: true,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default CodeImprovement;
