// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const ProConDiscusser = {
  api_url: BACKEND_API_URL + 'default-pro-con-discusser',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Pros and Cons Discusser",
  assistant_name: "Persephone",
  avatar_url: '../public/applications/ProConDiscusser/Persephone.svg',
  background_image_url: '../public/applications/ProConDiscusser/ProConDiscusser-bg.svg',
  welcome_message: `Hello, I'm Persephone, the most learned hipster in the galaxy. I can discuss the pros and cons of anything.`,
  example_prompts: [
    'a time travel machine',
    'eating the last everlasting gobstopper',
    'attending a chocolate factory tour',
  ],
  placeholder_text: `tell Persephone what to evaluate...`,
};

export default ProConDiscusser;
