// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const RapBattle = {
  api_url: BACKEND_API_URL + 'default-rap-battle',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Rap Battle Generator",
  assistant_name: "Rhea",
  avatar_url: '../public/applications/RapBattle/Rhea.svg',
  background_image_url: '../public/applications/RapBattle/RapBattle-bg.jpg',
  welcome_message: `Hello, I'm Rhea, and I can generate rap battles between your two favorite people`,
  example_prompts: [
    'Rap battle between Linus Torvalds and Bill Gates',
    'Rap battle between Dave Chappelle and Kevin Hart',
    'Rap battle between Ghandi and Martin Luther King Jr.',
  ],
  placeholder_text: `tell Rhea who will battle...`,
};

export default RapBattle;
