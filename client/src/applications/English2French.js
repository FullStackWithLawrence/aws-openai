// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-translation";

const English2French = {
  sidebar_title: "English to French Translator",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "English to French Translator",
  assistant_name: "Fleur",
  avatar_url: "/applications/English2French/Fleur.svg",
  background_image_url: "/applications/English2French/English2French-bg.jpg",
  welcome_message: `Hello, I'm Fleur, and I'm fluent in French. I can help you translate English to French.`,
  example_prompts: [],
  placeholder_text: `give Fleur something to translate...`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default English2French;
