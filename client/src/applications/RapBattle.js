// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const RapBattle = {
  api_url: BACKEND_API_URL + 'default-rap-battle',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Rap Battle Generator",
  assistant_name: "Rhea",
  avatar_url: '/applications/RapBattle/Rhea.svg',
  background_image_url: '/applications/RapBattle/RapBattle-bg.jpg',
  welcome_message: `Hello, I'm Rhea, and I can generate rap battles between your two favorite people`,
  example_prompts: [
    'Rap battle between Linus Torvalds and Bill Gates',
    'Rap battle between Dave Grohl and Barak Obama',
    'Rap battle between Ghandi and Martin Luther King Jr.',
    'Rap battle between Wayne Gretzky and Ronaldo',
  ],
  placeholder_text: `tell Rhea who will battle...`,
};

export default RapBattle;
