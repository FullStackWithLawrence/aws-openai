
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
  try {
    const response = await fetch(apiURL, init);
    const status = await response.status;
    const response_json = await response.json(); // Convert the ReadableStream to a JSON object
    const response_body = await response_json.body;

    // console.log('response', response);
    // console.log('status', response.status);

    if (response.ok) {
      return response_body;
    }
    else {
      let errTitle = 'Error ' + status;
      let errMessage = 'An unknown error occurred.';
      switch (status) {
        case 400:
          errMessage = response.statusText || response_body.message || 'The request was invalid.';
          break;
        case 500:
          errMessage = response.statusText || response_body.message || 'An internal server error occurred.';
          break;
        case 504:
          errMessage = response.statusText || 'Gateway timeout error. This is a known consequence of using AWS Lambda for integrations to the OpenAI API. Note that AWS Lambda has a hard 29 second timeout. If OpenAI requests take longer, which is frequently the case with chatgpt-4 then you will receive this error. If the timeout persists then you might try using chatgpt-3.5 instead as it is more performant.';
          break;
      }
      openChatModal(errTitle, errMessage);
    }
  } catch (error) {
    openChatModal('Error', error);
    return;
  }
}
