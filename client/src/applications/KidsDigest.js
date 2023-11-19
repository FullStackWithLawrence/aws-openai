// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-summarize";

const KidsDigest = {
  sidebar_title: "KidsDigest",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "KidsDigest",
  assistant_name: "Kent",
  avatar_url: "/applications/KidsDigest/Kent.svg",
  background_image_url: "/applications/KidsDigest/KidsDigest-bg.jpg",
  welcome_message: `Hello, I'm Kent, and I summarize any content so that a second-grade student can understand it.`,
  example_prompts: [],
  placeholder_text: `say something to Kent`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default KidsDigest;
