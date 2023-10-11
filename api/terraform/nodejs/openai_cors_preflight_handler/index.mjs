export const handler = async (event, context) => {
  const response = {
      statusCode: 200,
      headers: {
          "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET,OPTIONS,POST,PUT,PATCH,DELETE"
      },
      body: JSON.stringify('Hello from Lambda!'),
  };
  return response;
};
