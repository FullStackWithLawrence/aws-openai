//
// see: https://stackoverflow.com/questions/45576200/fetch-api-post-call-returning-403-forbidden-error-in-react-js-but-the-same-url-w
//      https://stackoverflow.com/questions/76182956/cors-preflight-response-error-with-aws-api-gateway-and-lambda-function
//
import { useState, useEffect } from 'react';
import './App.css';
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';
import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  TypingIndicator,
} from '@chatscope/chat-ui-kit-react';

// API_KEY access is scaffolded, but in point of fact it's not really
// necessary for this application since Terraform also creates an
// AWS API Gateway 'Usage Plan' that limits access to the API.
//
// The API_KEY is only used to demonstrate how you'd set this up in
// the event that you needed it.
const AWS_API_GATEWAY_KEY = 'Ddwuzmkd8z9tyAwenGrky5R47I0BsNvk5MY88qRn';

const App = () => {
  const [messages, setMessages] = useState([
    {
      message: "Hello, I'm an air travel chatbot powered by ChatGPT. Ask me anything about airport codes anywhere in the world!",
      sentTime: 'just now',
      sender: 'ChatGPT',
    },
  ]);
  const [isTyping, setIsTyping] = useState(false);

  const handleSendRequest = async (message) => {
    const newMessage = {
      message,
      direction: 'outgoing',
      sender: 'user',
    };

    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setIsTyping(true);

    try {
      const response = await processMessageToChatGPTApplication(message);
      if ("choices" in response) {
        const content = response.choices[0]?.message?.content;
        if (content) {
          const chatGPTResponse = {
            message: content,
            sender: 'ChatGPT',
          };
          setMessages((prevMessages) => [...prevMessages, chatGPTResponse]);
        }
      }
    } catch (error) {
      console.error('Error processing message:', error);
    } finally {
      setIsTyping(false);
    }
  };

  async function processMessageToChatGPTApplication(chatMessage) {
    const url = 'https://api.openai.lawrencemcdaniel.com/examples/default-airport-codes';
    const body = {
      'input_text': chatMessage
    };
    let headers = {
      'x-api-key': AWS_API_GATEWAY_KEY,
      'Accept': '*/*',
      'Content-Type': 'application/json'
    };
    const init = {
      // credentials: 'include',
      method: 'POST',
      // mode: 'no-cors',
      headers: headers,
      body: JSON.stringify(body),
    };
    console.log(url, init);
    const response = await fetch(url, init);
    if (response.ok) {
      const response_json = await response.json(); // Convert the ReadableStream to a JSON object
      console.log("success. response====", response_json);

      const body = response_json.body;
      console.log("success. body====", body);
      return body;
    } else {
      console.log("error: ", response.status);
      return {};
    }
  }

  return (
    <div className='App'>
      <div style={{ position: 'relative', height: '500px' }}>
        <MainContainer>
          <ChatContainer>
            <MessageList
              scrollBehavior='smooth'
              typingIndicator={isTyping ? <TypingIndicator content='ChatGPT is typing' /> : null}
            >
              {messages.map((message, i) => {
                console.log(message)
                return <Message key={i} model={message} />
              })}
            </MessageList>
            <MessageInput placeholder='Ask me anything' onSend={handleSendRequest} />
          </ChatContainer>
        </MainContainer>
      </div>
    </div>
  )
}

export default App
