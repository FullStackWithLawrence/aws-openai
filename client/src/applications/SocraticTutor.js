import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-socratic-tutor";

const SocraticTutor = {
  sidebar_title: "Socratic Tutor",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Socratic Tutor",
  assistant_name: "Seraphina",
  avatar_url: "/applications/SocraticTutor/Seraphina.svg",
  background_image_url: "/applications/SocraticTutor/SocraticTutor-bg.jpg",
  welcome_message: `Hello, I'm Seraphina, a disciple of the great philosopher, Socrates. I can help you learn about philosophy.`,
  example_prompts: [
    '"I think, therefore I am"',
    '"To be is to do"',
    '"Reality is merely an illusion, albeit a very persistent one"',
  ],
  placeholder_text: "tell Seraphina something deep...",
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default SocraticTutor;
