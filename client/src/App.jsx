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

const API_KEY = 'zz2qij7Vnh82wYUDhnQtX5DPO7Z054kt75KvMsp1'

const App = () => {
  const [messages, setMessages] = useState([
    {
      message: "Hello, I'm a ChatGPT custom application! Ask me anything!",
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
      'x-api-key': API_KEY,
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
    const response = await fetch(url, init)
      .then((response) => {
        console.log(response.status);
        console.log("success====", response);
        return response;
      })
      .catch((error) => {
        console.log("error=====", error);
        return {};
      });
    return response;
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
