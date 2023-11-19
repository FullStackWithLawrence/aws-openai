// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-parse-data";

const CSVify = {
  sidebar_title: "CSVify",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "CSVify",
  assistant_name: "Chad",
  avatar_url: "/applications/CSVify/Chad.svg",
  background_image_url: "/applications/CSVify/CSVify-bg.jpg",
  welcome_message: `Hello, I'm Chad, and I convert unstructured text data to CSV. Paste some text into the chat box to get started.`,
  example_prompts: [],
  placeholder_text: `send some data to Chad`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default CSVify;
