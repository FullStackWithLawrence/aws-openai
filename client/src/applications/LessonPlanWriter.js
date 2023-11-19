// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-lesson-plan-writer";

const LessonPlanWriter = {
  sidebar_title: "Lesson Plan Writer",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Lesson Plan Writer",
  assistant_name: "Langston",
  avatar_url: "/applications/LessonPlanWriter/Langston.svg",
  background_image_url:
    "/applications/LessonPlanWriter/LessonPlanWriter-bg.jpg",
  welcome_message: `Hello, I'm Langston, an education professional. I can help you write a lesson plan.`,
  example_prompts: [],
  placeholder_text: `tell Langston what the lesson is about...`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default LessonPlanWriter;
