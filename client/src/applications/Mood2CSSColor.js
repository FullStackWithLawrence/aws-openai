// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-mood-color";

const Mood2CSSColor = {
  sidebar_title: "Mood To CSS Color",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Mood2CSSColor",
  assistant_name: "Marlene",
  avatar_url: "/applications/Mood2CSSColor/Marlene.svg",
  background_image_url: "/applications/Mood2CSSColor/Mood2CSSColor-bg.jpg",
  welcome_message: `Hello, I'm Marlene, and I convert your mood into a CSS hex color code.`,
  example_prompts: [
    '"I am happy as a clam"',
    '"I am snug as a bug in a rug"',
    '"If I felt any better it would be illegal"',
  ],
  placeholder_text: `tell Marlene how you feel`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default Mood2CSSColor;
