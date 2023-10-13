// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const ProductNameGenerator = {
  api_url: BACKEND_API_URL + 'default-product-name-gen',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "ProductNameGenerator",
  assistant_name: "Peter",
  avatar_url: '../public/applications/ProductNameGenerator/Peter.svg',
  background_image_url: '../public/applications/ProductNameGenerator/ProductNameGenerator-bg.avif',
  welcome_message: `Hello, I'm Peter, and I create a list of potential product names based on your input.`,
  example_prompts: [],
  placeholder_text: `tell Peter about your product`,
};

export default ProductNameGenerator;
