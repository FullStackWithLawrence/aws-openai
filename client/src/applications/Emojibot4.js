// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const Emojibot4 = {
  api_url: BACKEND_API_URL + 'default-emoji-chatbot',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Emojibot gpt-4",
  assistant_name: "Matilda",
  avatar_url: '../public/applications/Emojibot4/Matilda.svg',
  background_image_url: '../public/applications/Emojibot4/Emojibot4-bg.jpg',
  welcome_message: `Hello, I'm Matilda, a mime created with gpt-4 who only responds with emojis. Let's chat!`,
  example_prompts: [
    "What's shake'n bacon",
    '"Lets go on a magic carpet ride"',
    '"Shooby dooby doo, where are are you"',
  ],
  placeholder_text: `say something to Matilda`,
};

export default Emojibot4;
