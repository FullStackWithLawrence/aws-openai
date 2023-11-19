// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-keywords";

const KeyWords = {
  sidebar_title: "KeyWord Generator",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "KeyWords",
  assistant_name: "Kiefer",
  avatar_url: "/applications/KeyWords/Kiefer.svg",
  background_image_url: "/applications/KeyWords/KeyWords-bg.png",
  welcome_message: `Hello, I'm Kiefer, and I will create a list of keywords from any content.`,
  example_prompts: [],
  placeholder_text: `send some text to Kiefer`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
  file_attach_button: false,
};

export default KeyWords;
