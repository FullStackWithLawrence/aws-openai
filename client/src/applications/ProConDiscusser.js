// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-pro-con-discusser";

const ProConDiscusser = {
  sidebar_title: "Pro and Con Discusser",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Pros and Cons Discusser",
  assistant_name: "Persephone",
  avatar_url: "/applications/ProConDiscusser/Persephone.svg",
  background_image_url: "/applications/ProConDiscusser/ProConDiscusser-bg.svg",
  welcome_message: `Hello, I'm Persephone, the most learned in the galaxy. I can discuss the pros and cons of anything.`,
  example_prompts: [
    "a time travel machine",
    "eating the last everlasting gobstopper",
    "attending a chocolate factory tour",
  ],
  placeholder_text: `tell Persephone what to evaluate...`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default ProConDiscusser;
