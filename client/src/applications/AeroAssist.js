import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-airport-codes";

const AeroAssist = {
  sidebar_title: "Airport Assistant",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Airport Assistant",
  assistant_name: "Emily",
  avatar_url:
    "https://chatscope.io/storybook/react/static/media/emily.d34aecd9.svg",
  background_image_url: "/applications/AeroAssist/AeroAssist-bg.svg",
  welcome_message: `Hello, I'm Emily, an air travel chatbot powered by ChatGPT. Ask me anything about airport codes anywhere in the world!`,
  example_prompts: [
    '"What is the airport code for London Heathrow?"',
    '"What is the largest airport in the world?"',
    '"Name an airport for private jets in Dallas Texas"',
    '"Name an airport in Mexico where you can land a helicopter"',
    '"I want to fly from Frankfurt to London."',
  ],
  placeholder_text: "Ask me anything about airports",
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default AeroAssist;
