//
// see: https://chatscope.io/storybook/react/?path=/story/documentation-introduction--page
//      https://stackoverflow.com/questions/45576200/fetch-api-post-call-returning-403-forbidden-error-in-react-js-but-the-same-url-w
//      https://stackoverflow.com/questions/76182956/cors-preflight-response-error-with-aws-api-gateway-and-lambda-function
//
import { useState, useEffect } from 'react';
import './Component.css';
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';


import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  TypingIndicator,
  MessageSeparator,

  Avatar,
  ConversationHeader,
  InfoButton,
  VoiceCallButton,
  VideoCallButton,
} from '@chatscope/chat-ui-kit-react';

const TIMESTAMP_NOW = 'just now';

async function processMessageToChatGPTApplication(chatMessage, apiURL, apiKey) {
  const init = {
    method: 'POST',
    headers: {
      'x-api-key': apiKey,
      'Accept': '*/*',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'input_text': chatMessage
    }),
  };
  const response = await fetch(apiURL, init);
  if (response && response.ok) {
    const response_json = await response.json(); // Convert the ReadableStream to a JSON object
    const response_body = response_json.body;
    console.log("body", response_body);
    return response_body;
  } else {
    console.log("error", response);
    return {};
  }
}

const examplePrompts = (exampleProps) => {
  return 'Some example prompts to get you started:\r\n\r\n' + exampleProps.map((prompt) => {return prompt + '\r\n'}).join('');
}

const ChatApp = (props) => {
  const [messages, setMessages] = useState([
    {
      message: props.welcome_message,
      sentTime: TIMESTAMP_NOW,
      sender: props.app_name,
    },
    {
      message: examplePrompts(props.example_prompts),
      sentTime: TIMESTAMP_NOW,
      sender: props.app_name,
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
      const response = await processMessageToChatGPTApplication(message, props.api_url, props.api_key);

      if ("choices" in response) { // simple way to ensure that we received a valid response
        const content = response.choices[0]?.message?.content;
        if (content) {
          const chatGPTResponse = {
            message: content,
            sender: props.app_name,
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

  const transparentBackgroundStyle = {
    backgroundColor: 'rgba(0,0,0,0.10)',
    color: 'lightgray',
  };
  const MainContainerStyle = {
    backgroundImage: "url('" + props.background_image_url + "')",
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    height: '100%',
  };
  return(
    <div style={{ position: 'relative', height: '100%' }}>
        <MainContainer style={MainContainerStyle} >
            <ChatContainer style={transparentBackgroundStyle} >
              <ConversationHeader>
                <Avatar src={props.avatar_url} name={props.app_name} />
                <ConversationHeader.Content userName={props.app_name} info="Active 10 mins ago" />
                <ConversationHeader.Actions>
                  <VoiceCallButton disabled />
                  <VideoCallButton disabled />
                  <InfoButton />
              </ConversationHeader.Actions>
              </ConversationHeader>
              <MessageList
                style={transparentBackgroundStyle}
                scrollBehavior='smooth'
                typingIndicator={isTyping ? <TypingIndicator content={props.assistant_name + ' is typing'} style={transparentBackgroundStyle} /> : null}
              >
                <MessageSeparator content="Monday, 23 December 2019" as="h2" style={transparentBackgroundStyle} />
                {messages.map((message, i) => {
                  return <Message key={i} model={message} />
                })}
              </MessageList>
              <MessageInput
                placeholder={props.placeholder_text}
                onSend={handleSendRequest}
                attachButton={false}
                fancyScroll={false}
                backgroundColor='lightgray'
                />
            </ChatContainer>
          </MainContainer>
    </div>
  )
}

export default ChatApp;
