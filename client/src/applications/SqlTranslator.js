// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const SqlTranslator = {
  api_url: BACKEND_API_URL + 'default-sql-translate',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "SQL Translator",
  assistant_name: "Svea",
  avatar_url: '../public/applications/SqlTranslator/Svea.svg',
  background_image_url: '../public/applications/SqlTranslator/SqlTranslator-bg.svg',
  welcome_message: `Hello, I'm Svea, a senior SQL database engineer. I can help you create SQL queries.`,
  example_prompts: [],
  placeholder_text: `send some data to Svea`,
};

export default SqlTranslator;
