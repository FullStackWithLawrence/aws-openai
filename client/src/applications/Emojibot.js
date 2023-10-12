// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const Emojibot = {
  api_url: BACKEND_API_URL + 'default-emoji-translation',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Emojibot",
  assistant_name: "Erik",
  avatar_url: '../public/applications/Emojibot/Erik.svg',
  background_image_url: '../public/applications/Emojibot/Emojibot-bg.jpg',
  welcome_message: `Hello, I'm Erik, and I only respond with emojis. Let's chat!`,
  example_prompts: [
    "What's shake'n bacon",
    '"Lets go on a magic carpet ride"',
    '"Shooby dooby doo, where are are you"',
  ],
  placeholder_text: `say something to Erik`,
};

export default Emojibot;
