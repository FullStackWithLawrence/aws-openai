// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const SpreadsheetGenerator = {
  api_url: BACKEND_API_URL + 'default-product-name-gen',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Spreadsheet Generator",
  assistant_name: "Sarah",
  avatar_url: '/applications/SpreadsheetGenerator/Sarah.svg',
  background_image_url: '/applications/SpreadsheetGenerator/SpreadsheetGenerator-bg.svg',
  welcome_message: `Hello, I'm Sarah, and I create spreadsheets from the data you give me.`,
  example_prompts: [],
  placeholder_text: `send some data to Sarah`,
};

export default SpreadsheetGenerator;
