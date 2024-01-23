//---------------------------------------------------------------------------------
//  written by: Lawrence McDaniel
//              https://lawrencemcdaniel.com
//
//  date:       Oct-2023
//---------------------------------------------------------------------------------

// React stuff
import React, { useRef } from "react";
import { useState } from "react";
import PropTypes from "prop-types";

// Chat UI stuff
import "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";
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
} from "@chatscope/chat-ui-kit-react";

// Our stuff
import "./Component.css";
import { ChatModal } from "./Modal.jsx";
import { processApiRequest } from "./ApiRequest.js";
import { ErrorBoundary } from "./errorBoundary.jsx";

function ChatApp(props) {
  const fileInputRef = useRef(null);

  // props. These are passed in from the parent component.
  // In all fairness this probably isn't necessary, but it's a good practice
  // to define the props that are expected to be passed in and also
  // to make these immutable.
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
  const uses_openai = props.uses_openai;
  const uses_openai_api = props.uses_openai_api;
  const uses_langchain = props.uses_langchain;
  const uses_memory = props.uses_memory;

  const [isTyping, setIsTyping] = useState(false);
  const [llm, setLLM] = useState("");

  function conversationHeaderFactory() {
    let conversation_header = "";
    if (uses_openai_api) {
      conversation_header = "OpenAI API";
    }
    if (uses_langchain) {
      conversation_header = "Langchain";
      if (uses_memory && uses_langchain) {
        conversation_header = conversation_header + " with Memory";
      }
      if (uses_openai) {
        conversation_header = conversation_header + " running OpenAI LLM";
      }
    }
    if (llm != "") {
      conversation_header = conversation_header + " " + llm;
    }
    return conversation_header;
  }

  function convertMarkdownLinksToHTML(message) {
    const markdownLinkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
    return message.replace(markdownLinkRegex, '<a href="$2">$1</a>');
  }

  function messageFactory(message, direction, sender) {
    const converted_message = convertMarkdownLinksToHTML(message);
    return {
      message: converted_message,
      direction: direction,
      sentTime: new Date().toLocaleString(),
      sender: sender,
    };
  }

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
  const [modalMessage, setmodalMessage] = useState("");
  const [modalTitle, setmodalTitle] = useState("");

  // prompt hints
  const examplePrompts = (prompts) => {
    if (prompts.length == 0) {
      return "";
    } else
      return (
        "Some example prompts to get you started:\r\n\r\n" +
        prompts
          .map((prompt) => {
            return prompt + "\r\n";
          })
          .join("")
      );
  };

  // message thread content
  const examples = examplePrompts(example_prompts);
  let message_items = [messageFactory(welcome_message, "incoming", "system")];
  if (examples) {
    message_items.push(messageFactory(examples, "incoming", "system"));
  }
  const [messages, setMessages] = useState(message_items);

  // UI widget event handlers
  const handleInfoButtonClick = () => {
    window.open(info_url, "_blank");
  };

  // API request handler
  async function handleRequest(input_text, base64_encode = true) {
    const newMessage = messageFactory(input_text, "outgoing", "user");
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setIsTyping(true);

    try {
      let response;
      if (base64_encode) {
        // uploaded files need to be base64 encoded.
        response = await processApiRequest(
          btoa(input_text),
          messages,
          api_url,
          api_key,
          openChatModal,
        );
      } else {
        // everything else is passed as plain text
        response = await processApiRequest(
          input_text,
          messages,
          api_url,
          api_key,
          openChatModal,
        );
      }
      // FIX NOTE: THIS IS A HACK, AND ITS STUPIDLY REPETITIVE. REFACTOR THIS.
      // Legacy OpenAI API
      if (
        response &&
        "chat_memory" in response &&
        "messages" in response.chat_memory
      ) {
        const aiMessage = response.chat_memory.messages.find(
          (message) => message.type === "ai",
        );
        if (aiMessage) {
          const content = aiMessage.content;
          if (content) {
            const chatGPTResponse = messageFactory(
              content,
              "incoming",
              "assistant",
            );
            setMessages((prevMessages) => [...prevMessages, chatGPTResponse]);
          }
          const llm_response = response.request_meta_data.model;
          setLLM(llm_response);
        }
      }
      // LangChain
      if (response && "choices" in response) {
        const content = response.choices[0]?.message?.content;
        if (content) {
          const chatGPTResponse = messageFactory(
            content,
            "incoming",
            "assistant",
          );
          setMessages((prevMessages) => [...prevMessages, chatGPTResponse]);
        }
        const llm_response = response.request_meta_data.model;
        setLLM(llm_response);
      }
    } catch (error) {
      // FIX NOTE: ADD MODAL HERE
      console.error("Exception:", error);
    } finally {
      setIsTyping(false);
    }
  }

  // file upload event handlers
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

  // send button event handler
  const handleSendRequest = (input_text) => {
    // remove any HTML tags from the input_text. Pasting text into the
    // input box (from any source) tends to result in HTML span tags being included
    // in the input_text. This is a problem because the API doesn't know how to
    // handle HTML tags. So we remove them here.
    const sanitized_input_text = input_text.replace(/<[^>]+>/g, "");

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
    backgroundColor: "rgba(0,0,0,0.10)",
    color: "lightgray",
  };
  const MainContainerStyle = {
    backgroundImage:
      "linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, .75)), url('" +
      background_image_url +
      "')",
    backgroundSize: "cover",
    backgroundPosition: "center",
    height: "100%",
  };

  // render the chat app
  return (
    <div className="chat-app">
      <MainContainer style={MainContainerStyle}>
        <ErrorBoundary>
          <ChatModal
            isModalOpen={isModalOpen}
            title={modalTitle}
            message={modalMessage}
            onCloseClick={closeChatModal}
          />
        </ErrorBoundary>
        <ChatContainer style={transparentBackgroundStyle}>
          <ConversationHeader>
            <Avatar src={avatar_url} name={app_name} />
            <ConversationHeader.Content
              userName={app_name}
              info={conversationHeaderFactory()}
            />
            <ConversationHeader.Actions>
              <VoiceCallButton disabled />
              <VideoCallButton disabled />
              <InfoButton onClick={handleInfoButtonClick} title={info_url} />
            </ConversationHeader.Actions>
          </ConversationHeader>
          <MessageList
            style={transparentBackgroundStyle}
            scrollBehavior="smooth"
            typingIndicator={
              isTyping ? (
                <TypingIndicator content={assistant_name + " is typing"} />
              ) : null
            }
          >
            {messages.map((message, i) => {
              return <Message key={i} model={message} />;
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
        <input
          type="file"
          accept=".py"
          title="Select a Python file"
          ref={fileInputRef}
          style={{ display: "none" }}
          onChange={handleFileChange}
        />
      </MainContainer>
    </div>
  );
}

// define the props that are expected to be passed in and also
// make these immutable.
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
  uses_openai: PropTypes.bool.isRequired,
  uses_openai_api: PropTypes.bool.isRequired,
  uses_langchain: PropTypes.bool.isRequired,
  uses_memory: PropTypes.bool.isRequired,
};

export default ChatApp;
