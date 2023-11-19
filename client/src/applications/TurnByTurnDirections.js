// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-turn-by-turn-directions";

const TurnByTurnDirections = {
  sidebar_title: "Turn By Turn Directions",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Turn By Turn Directions",
  assistant_name: "Nancy",
  avatar_url: "/applications/TurnByTurnDirections/Nancy.svg",
  background_image_url:
    "/applications/TurnByTurnDirections/TurnByTurnDirections-bg.svg",
  welcome_message: `Hello, I'm Nancy, an expert navigator and I provide turn by turn directions.`,
  example_prompts: [],
  placeholder_text: `tell Nancy where you want to go`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default TurnByTurnDirections;
