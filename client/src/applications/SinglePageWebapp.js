import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const SinglePageWebapp = {
  api_url: BACKEND_API_URL + 'default-single-page-websit',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Single Page Webapp Creator",
  assistant_name: "Sybil",
  avatar_url: '../public/applications/SinglePageWebapp/Sybil.svg',
  background_image_url: '../public/applications/SinglePageWebapp/SinglePageWebapp-bg.svg',
  welcome_message: `Hello, I'm Sybil, a Python programmer. I can help you create a single page web app using a Python framework. `,
  example_prompts: [
    '"make a hello world app"',
    '"make a todo list app"',
    '"make a recipe app"',
  ],
  placeholder_text: 'tell Sybil what you want to create...',
};

export default SinglePageWebapp;
