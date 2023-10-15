//---------------------------------------------------------------------------------
//  written by: Lawrence McDaniel
//              https://lawrencemcdaniel.com
//
//  date:       Oct-2023
//---------------------------------------------------------------------------------
import React, { useRef } from 'react';
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

import { ChatModal } from './Modal.jsx';
import { processApiRequest } from './ApiRequest.js';

const TIMESTAMP_NOW = 'just now';
function ChatApp(props) {
  const fileInputRef = useRef(null);

  // props
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
  const file_attach_button = props.file_attach_button;

  // Error modal state management
  function openChatModal(title, msg) {
    setIsModalOpen(true);
    setmodalTitle(title);
    setmodalMessage(msg);
  }
  function closeChatModal() {
    setIsModalOpen(false);
  }
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalMessage, setmodalMessage] = useState('');
  const [modalTitle, setmodalTitle] = useState('');

  // prompt hints
  const examplePrompts = (prompts) => {
    if (prompts.length == 0) {
      return '';
    } else return 'Some example prompts to get you started:\r\n\r\n' + prompts.map((prompt) => {return prompt + '\r\n'}).join('');
  }

  // message thread content
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

  // UI widget event handlers
  const handleInfoButtonClick = () => {
    window.open(info_url, '_blank');
  };
  async function handleRequest(input_text, base64_encode=true) {
    const newMessage = {
      message: input_text,
      direction: 'outgoing',
      sender: 'user',
    };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setIsTyping(true);

    try {
      let response;
      if (base64_encode) {
        response = await processApiRequest(btoa(input_text), api_url, api_key, openChatModal);
      } else {
        response = await processApiRequest(input_text, api_url, api_key, openChatModal);
      }

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
  }

  const handleAttachClick = async () => {
    fileInputRef.current.click();
  };
  function handleFileChange(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = (event) => {
      const fileContent = event.target.result;
      handleRequest(fileContent, true);
    };
    reader.readAsText(file);
  }
  const handleSendRequest = (input_text) => {

    // remove any HTML tags from the input_text
    const sanitized_input_text = input_text.replace(/<[^>]+>/g, '');

    // check if the sanitized input text is empty or only contains whitespace
    if (!sanitized_input_text.trim()) {
      return;
    }

    handleRequest(sanitized_input_text, false);
  };


  // UI widget styles
  // note that most styling is intended to be created in Component.css
  // these are outlying cases where inline styles are required in order to override the default styles
  const transparentBackgroundStyle = {
    backgroundColor: 'rgba(0,0,0,0.10)',
    color: 'lightgray',
  };
  const MainContainerStyle = {
    backgroundImage: "linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, .75)), url('" + background_image_url + "')",
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    height: '100%',
  };

  // render the chat app
  return(
    <div className='chat-app'>
      <MainContainer style={MainContainerStyle} >
        <ChatModal isModalOpen={isModalOpen} title={modalTitle} message={modalMessage} onCloseClick={closeChatModal} />
        <ChatContainer style={transparentBackgroundStyle} >
          <ConversationHeader>
            <Avatar src={avatar_url} name={app_name} />
            <ConversationHeader.Content userName={app_name} info="online" />
            <ConversationHeader.Actions>
              <VoiceCallButton disabled />
              <VideoCallButton disabled />
              <InfoButton onClick={handleInfoButtonClick} title={info_url} />
          </ConversationHeader.Actions>
          </ConversationHeader>
          <MessageList
            style={transparentBackgroundStyle}
            scrollBehavior='smooth'
            typingIndicator={isTyping ? <TypingIndicator content={assistant_name + ' is typing'} /> : null}
          >
            {messages.map((message, i) => {
              return <Message key={i} model={message} />
            })}
          </MessageList>
          <MessageInput
            placeholder={placeholder_text}
            onSend={handleSendRequest}
            onAttachClick={handleAttachClick}
            attachButton={file_attach_button}
            fancyScroll={false}
            />
        </ChatContainer>
        <input type="file" accept=".py" title="Select a Python file" ref={fileInputRef} style={{ display: 'none' }} onChange={handleFileChange} />
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
  file_attach_button: PropTypes.bool.isRequired,
};

export default ChatApp;
