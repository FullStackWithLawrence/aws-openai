
export async function processApiRequest(chatMessage, apiURL, apiKey) {
  const init = {
    method: 'POST',
    mode: 'cors',
    headers: {
      'x-api-key': apiKey,
      'Accept': '*/*',
      'Content-Type': 'application/json',
      'Origin': window.location.origin
    },
    body: JSON.stringify({
      'input_text': chatMessage
    }),
  };
  try {
    const response = await fetch(apiURL, init);
    const response_json = await response.json(); // Convert the ReadableStream to a JSON object
    return {
      'status': response.status,
      'statusText': response.statusText,
      'ok': response.ok,
      'json': response_json
    };
  } catch (error) {
    return {};
  }
}
