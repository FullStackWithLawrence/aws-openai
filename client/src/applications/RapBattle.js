// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-rap-battle";

const RapBattle = {
  sidebar_title: "Rap Battle Generator",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Rap Battle Generator",
  assistant_name: "Rhea",
  avatar_url: "/applications/RapBattle/Rhea.svg",
  background_image_url: "/applications/RapBattle/RapBattle-bg.jpg",
  welcome_message: `Hello, I'm Rhea, and I can generate rap battles between your two favorite people`,
  example_prompts: [
    "Linus Torvalds vs Bill Gates",
    "Dave Grohl vs Barack Obama",
    "Gandhi vs Martin Luther King Jr.",
    "Wayne Gretzky vs Ronaldo",
  ],
  placeholder_text: `tell Rhea who will battle...`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default RapBattle;
