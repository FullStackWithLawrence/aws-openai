import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const appAeroAssist = {
  api_url: BACKEND_API_URL,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "AeroAssist",
  avatar_url: 'https://chatscope.io/storybook/react/static/media/emily.d34aecd9.svg',
  welcome_message: "Hello, I'm an air travel chatbot powered by ChatGPT. Ask me anything about airport codes anywhere in the world!",
  example_prompts: [
    '"What is the airport code for London Heathrow?"',
    '"What is the largest airport in the world?"',
    '"Name an airport for private jets in Dallas Texas"',
    '"Name an airport in Mexico where you can land a helicopter"',
    '"I want to fly from Frankfurt to London."',
  ],
  placeholder_text: 'Ask me anything about airports',
};

export default appAeroAssist;
