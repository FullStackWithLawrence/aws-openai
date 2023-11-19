// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-emoji-translation";

const Emojibot = {
  sidebar_title: "Emoji Translator",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Emojibot",
  assistant_name: "Erik",
  avatar_url: "/applications/Emojibot/Erik.svg",
  background_image_url: "/applications/Emojibot/Emojibot-bg.jpg",
  welcome_message: `Hello, I'm Erik, and I will translate your text into emojis.`,
  example_prompts: [
    "What's shake'n bacon",
    '"Lets go on a magic carpet ride"',
    '"Shooby dooby doo, where are are you"',
  ],
  placeholder_text: `type something for Erik to translate into emojis`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default Emojibot;
