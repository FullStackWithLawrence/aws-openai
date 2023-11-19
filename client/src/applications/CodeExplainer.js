// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-explain-code";

const CodeExplainer = {
  sidebar_title: "Code Explainer",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "CodeExplainer",
  assistant_name: "Patricia",
  avatar_url: "/applications/CodeExplainer/Patricia.svg",
  background_image_url: "/applications/CodeExplainer/CodeExplainer-bg.svg",
  welcome_message: `Hello, I'm Patricia and I'm an expert Python programmer. Upload a Python file and I'll concisely explain what it does.`,
  example_prompts: [],
  placeholder_text: `upload a Python file`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: true,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default CodeExplainer;
