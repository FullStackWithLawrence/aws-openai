import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-single-page-websit";

const SinglePageWebapp = {
  sidebar_title: "Single Page Webapp Creator",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Single Page Webapp Creator",
  assistant_name: "Sybil",
  avatar_url: "/applications/SinglePageWebapp/Sybil.svg",
  background_image_url:
    "/applications/SinglePageWebapp/SinglePageWebapp-bg.svg",
  welcome_message: `Hello, I'm Sybil, a Python programmer. I can help you create a single page web app using a Python framework. `,
  example_prompts: [
    '"make a hello world app"',
    '"make a todo list app"',
    '"make a recipe app"',
  ],
  placeholder_text: "tell Sybil what you want to create...",
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default SinglePageWebapp;
