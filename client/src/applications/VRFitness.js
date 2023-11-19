// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-vr-fitness";

const VRFitness = {
  sidebar_title: "VR Fitness",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "VR Fitness",
  assistant_name: "Francesca",
  avatar_url: "/applications/VRFitness/Francesca.svg",
  background_image_url: "/applications/VRFitness/VRFitness-bg.jpg",
  welcome_message: `Hello, I'm Francesca, and I can help you create a VR fitness routine.`,
  example_prompts: [],
  placeholder_text: `tell Francesca about your exercise idea`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default VRFitness;
