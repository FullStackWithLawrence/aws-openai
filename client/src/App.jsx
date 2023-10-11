import { useState, useEffect }  from 'react';
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

const API_KEY ='uPFeMkVW6WaoVMba4wRSd6MIOG8kSF9n7axQpHdT'

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
      const content = response.choices[0]?.message?.content;
      if (content) {
        const chatGPTResponse = {
          message: content,
          sender: 'ChatGPT',
        };
        setMessages((prevMessages) => [...prevMessages, chatGPTResponse]);
      }
    } catch (error) {
      console.error('Error processing message:', error);
    } finally {
      setIsTyping(false);
    }
  };

  async function processMessageToChatGPTApplication(chatMessage) {
    const url = 'https://api.openai.lawrencemcdaniel.com/examples/default-emoji-chatbot';
    const apiRequestBody = {
      'input_text': chatMessage
    };
    let headers = {
      'Content-Type': 'application/json',
      'x-api-key': API_KEY,
      'Accept': '*/*',
      'Accept-Encoding': 'gzip, deflate, br',
      'Connection': 'keep-alive',
      'User-Agent': 'ReactJS'
    };

    const init = {
      method: 'POST',
      mode: 'no-cors',
      headers: headers,
      body: JSON.stringify(apiRequestBody),
    };
    console.log('args', init);
    const response = await fetch(url, init);
    const data = await response.json();
    return data;
  }

  return (
    <div className='App'>
      <div style={{ position:'relative', height: '500px'  }}>
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
