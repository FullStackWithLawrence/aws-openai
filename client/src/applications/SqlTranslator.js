// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-sql-translate";

const SqlTranslator = {
  sidebar_title: "SQL Translator",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "SQL Translator",
  assistant_name: "Svea",
  avatar_url: "/applications/SqlTranslator/Svea.svg",
  background_image_url: "/applications/SqlTranslator/SqlTranslator-bg.svg",
  welcome_message: `Hello, I'm Svea, a senior SQL database engineer. I can help you create SQL queries.`,
  example_prompts: [],
  placeholder_text: `send some data to Svea`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default SqlTranslator;
