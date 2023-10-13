// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const Mood2CSSColor = {
  api_url: BACKEND_API_URL + 'default-mood-color',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Mood2CSSColor",
  assistant_name: "Marlene",
  avatar_url: '../public/applications/Mood2CSSColor/Marlene.svg',
  background_image_url: '../public/applications/Mood2CSSColor/Mood2CSSColor-bg.jpg',
  welcome_message: `Hello, I'm Marlene, and I convert your mood into a CSS hex color code.`,
  example_prompts: [
    '"I am happy as a clam"',
    '"I am snug as a bug in a rug"',
    '"If I felt any better it would be illegal"',
  ],
  placeholder_text: `tell Marlene how you feel`,
};

export default Mood2CSSColor;
