
export async function processApiRequest(chatMessage, apiURL, apiKey, openChatModal) {
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
  const response = await fetch(apiURL, init);
  if (response && response.ok) {
    const response_json = await response.json(); // Convert the ReadableStream to a JSON object
    const response_body = response_json.body;
    return response_body;
  } else {
    openChatModal(response);
    return {};
  }
}
