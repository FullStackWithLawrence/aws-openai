// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-grammar";

const GrammarGenius = {
  sidebar_title: "Grammar Genius",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "GrammarGenius",
  assistant_name: "Gertrude",
  avatar_url: "/applications/GrammarGenius/Gertrude.svg",
  background_image_url: "/applications/GrammarGenius/GrammarGenius-bg.jpg",
  welcome_message: `Hello, I'm Gertrude, an English grammar chatbot powered by ChatGPT. You can practice your English grammar with me!`,
  example_prompts: [
    '"I broked my leg."',
    '"She do her homework."',
    '"The cat, running quickly, was chased by the dog."',
    '"I dont need no help"',
    '"He eats lunch, then he will go to the store."',
  ],
  placeholder_text: `say something to Gertrude`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default GrammarGenius;
