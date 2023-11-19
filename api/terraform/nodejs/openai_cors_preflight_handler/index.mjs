export const handler = async (event) => {
  // Scaffolding for CORS preflight response object.
  //
  // Creates a Lambda Proxy response with CORS headers.
  // https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html?shortFooter=true#api-gateway-simple-proxy-for-lambda-output-format
  const cors_headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Headers":
      "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET,OPTIONS,POST,PUT",
  };

  const response = {
    isBase64Encoded: false,
    statusCode: 200,
    headers: cors_headers,
    multiValueHeaders: {},
    body: JSON.stringify({
      message: "Hello from AWS Lambda Node.js",
    }),
  };

  return response;
};
