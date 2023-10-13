// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const VRFitness = {
  api_url: BACKEND_API_URL + 'default-vr-fitness',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "VR Fitness",
  assistant_name: "Francesca",
  avatar_url: '/applications/VRFitness/Francesca.svg',
  background_image_url: '/applications/VRFitness/VRFitness-bg.jpg',
  welcome_message: `Hello, I'm Francesca, and I can help you create a VR fitness routine.`,
  example_prompts: [],
  placeholder_text: `tell Francesca about your exercise idea`,
};

export default VRFitness;
