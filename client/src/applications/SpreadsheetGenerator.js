// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "default-product-name-gen";

const SpreadsheetGenerator = {
  sidebar_title: "Spreadsheet Generator",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Spreadsheet Generator",
  assistant_name: "Sarah",
  avatar_url: "/applications/SpreadsheetGenerator/Sarah.svg",
  background_image_url:
    "/applications/SpreadsheetGenerator/SpreadsheetGenerator-bg.svg",
  welcome_message: `Hello, I'm Sarah, and I create spreadsheets from the data you give me.`,
  example_prompts: [],
  placeholder_text: `send some data to Sarah`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: true,
  uses_openai: true,
  uses_openai_api: true,
  uses_langchain: false,
  uses_memory: false,
};

export default SpreadsheetGenerator;
