// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const KidsDigest = {
  api_url: BACKEND_API_URL + 'default-summarize',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "KidsDigest",
  assistant_name: "Kent",
  avatar_url: '../public/applications/KidsDigest/Kent.svg',
  background_image_url: '../public/applications/KidsDigest/KidsDigest-bg.jpg',
  welcome_message: `Hello, I'm Kent, and I summarize any content so that a second-grade student can understand it.`,
  example_prompts: [],
  placeholder_text: `say something to Kent`,
};

export default KidsDigest;
