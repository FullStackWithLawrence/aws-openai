// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const PythonDebugger = {
  api_url: BACKEND_API_URL + 'default-fix-python-bugs',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Python Debugger",
  assistant_name: "Deborah",
  avatar_url: '/applications/PythonDebugger/Deborah.svg',
  background_image_url: '/applications/PythonDebugger/PythonDebugger-bg.svg',
  welcome_message: `Hello, I'm Deborah, and I can debug Python code.`,
  example_prompts: [],
  placeholder_text: `upload a Python file for Deborah to debug`,
};

export default PythonDebugger;
