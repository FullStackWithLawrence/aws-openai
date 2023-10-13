import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const SocraticTutor = {
  api_url: BACKEND_API_URL + 'default-socratic-tutor',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Socratic Tutor",
  assistant_name: "Seraphina",
  avatar_url: '/applications/SocraticTutor/Seraphina.svg',
  background_image_url: '/applications/SocraticTutor/SocraticTutor-bg.jpg',
  welcome_message: `Hello, I'm Seraphina, a disciple of the great philosopher, Socrates. I can help you learn about philosophy.`,
  example_prompts: [
    '"I think, therefore I am"',
    '"To be is to do"',
    '"Reality is merely an illusion, albeit a very persistent one"',
  ],
  placeholder_text: 'tell Seraphina something deep...',
};

export default SocraticTutor;
