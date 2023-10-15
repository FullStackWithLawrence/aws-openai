// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import { BACKEND_API_URL, AWS_API_GATEWAY_KEY, OPENAI_EXAMPLES_URL } from "../config";

const SLUG = 'default-marv-sarcastic-chat';

const SarcasticChat = {
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Marv the Sarcastic Chatbot",
  assistant_name: "Marv",
  avatar_url: '/applications/SarcasticChat/Marv.svg',
  background_image_url: '/applications/SarcasticChat/SarcasticChat-bg.png',
  welcome_message: `Hello, I'm Marv, a sarcastic chatbot.`,
  example_prompts: [],
  placeholder_text: `say something to Marv`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
};

export default SarcasticChat;
