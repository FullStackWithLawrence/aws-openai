// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const MemoWriter = {
  api_url: BACKEND_API_URL + 'default-memo-writer',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Memo Writer",
  assistant_name: "Guillermo",
  avatar_url: '../public/applications/MemoWriter/Guillermo.svg',
  background_image_url: '../public/applications/MemoWriter/MemoWriter-bg.jpg',
  welcome_message: `Hello, I'm Guillermo, an executive assistant who can help you write a memo.`,
  example_prompts: [],
  placeholder_text: `tell Guillermo what this memo is about`,
};

export default MemoWriter;
