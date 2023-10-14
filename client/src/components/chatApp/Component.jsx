//
// see: https://chatscope.io/storybook/react/?path=/story/documentation-introduction--page
//      https://stackoverflow.com/questions/45576200/fetch-api-post-call-returning-403-forbidden-error-in-react-js-but-the-same-url-w
//      https://stackoverflow.com/questions/76182956/cors-preflight-response-error-with-aws-api-gateway-and-lambda-function
//
import React from 'react';
import { useState } from 'react';
import PropTypes from 'prop-types';

import './Component.css';
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';


import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  TypingIndicator,

  Avatar,
  ConversationHeader,
  InfoButton,
  VoiceCallButton,
  VideoCallButton,
} from '@chatscope/chat-ui-kit-react';

const TIMESTAMP_NOW = 'just now';

async function processApiRequest(chatMessage, apiURL, apiKey) {
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
    console.log("error", response);
    return {};
  }
}

const examplePrompts = (prompts) => {
  if (prompts.length == 0) {
    return '';
  } else return 'Some example prompts to get you started:\r\n\r\n' + prompts.map((prompt) => {return prompt + '\r\n'}).join('');
}

function ChatApp(props) {
  const welcome_message = props.welcome_message;
  const placeholder_text = props.placeholder_text;
  const api_url = props.api_url;
  const api_key = props.api_key;
  const app_name = props.app_name;
  const assistant_name = props.assistant_name;
  const avatar_url = props.avatar_url;
  const background_image_url = props.background_image_url;
  const info_url = props.info_url;
  const example_prompts = props.example_prompts;


  const examples = examplePrompts(example_prompts);
  let message_items = [{
    message: welcome_message,
    sentTime: TIMESTAMP_NOW,
    sender: app_name,
  }];
  if (examples) {
    message_items.push({
      message: examples,
      sentTime: TIMESTAMP_NOW,
      sender: app_name,
    });
  }
  const [messages, setMessages] = useState(message_items);
  const [isTyping, setIsTyping] = useState(false);

  const handleInfoButtonClick = () => {
    // FIX NOTE: implement me
    return (
      <div></div>
    )
  };
  const handleSendRequest = async (input_text) => {

    // remove any HTML tags from the input_text
    const sanitized_input_text = input_text.replace(/<[^>]+>/g, '');

    // check if the sanitized input text is empty or only contains whitespace
    if (!sanitized_input_text.trim()) {
      return;
    }

    const newMessage = {
      message: sanitized_input_text,
      direction: 'outgoing',
      sender: 'user',
    };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setIsTyping(true);

    try {
      const response = await processApiRequest(sanitized_input_text, api_url, api_key);

      if ("choices" in response) { // simple way to ensure that we received a valid response
        const content = response.choices[0]?.message?.content;
        if (content) {
          const chatGPTResponse = {
            message: content,
            sender: app_name,
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
    backgroundImage: "url('" + background_image_url + "')",
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    height: '100%',
  };
  return(
    <div className='chat-app'>
        <MainContainer style={MainContainerStyle} >
            <ChatContainer style={transparentBackgroundStyle} >
              <ConversationHeader>
                <Avatar src={avatar_url} name={app_name} />
                <ConversationHeader.Content userName={app_name} info="online" />
                <ConversationHeader.Actions>
                  <VoiceCallButton disabled />
                  <VideoCallButton disabled />
                  <InfoButton onClick={handleInfoButtonClick} />
              </ConversationHeader.Actions>
              </ConversationHeader>
              <MessageList
                style={transparentBackgroundStyle}
                scrollBehavior='smooth'
                typingIndicator={isTyping ? <TypingIndicator content={assistant_name + ' is typing'} style={transparentBackgroundStyle} /> : null}
              >
                {messages.map((message, i) => {
                  return <Message key={i} model={message} />
                })}
              </MessageList>
              <MessageInput
                placeholder={placeholder_text}
                onSend={handleSendRequest}
                attachButton={false}
                fancyScroll={false}
                />
            </ChatContainer>
          </MainContainer>
    </div>
  )
}

ChatApp.propTypes = {
  welcome_message: PropTypes.string.isRequired,
  placeholder_text: PropTypes.string.isRequired,
  api_url: PropTypes.string.isRequired,
  api_key: PropTypes.string.isRequired,
  app_name: PropTypes.string.isRequired,
  assistant_name: PropTypes.string.isRequired,
  avatar_url: PropTypes.string.isRequired,
  background_image_url: PropTypes.string.isRequired,
  info_url: PropTypes.string.isRequired,
  example_prompts: PropTypes.array.isRequired,
};

export default ChatApp;
