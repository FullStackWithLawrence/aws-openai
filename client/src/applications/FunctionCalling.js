// see https://platform.openai.com/docs/guides/function-calling
import {
  BACKEND_API_URL,
  AWS_API_GATEWAY_KEY,
  OPENAI_EXAMPLES_URL,
} from "../config";

const SLUG = "openai-function-calling";

const FunctionCalling = {
  sidebar_title: "OpenAI Function Calling",
  api_url: BACKEND_API_URL + SLUG,
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "OpenAI Function Calling",
  assistant_name: "Lawrence McDaniel",
  avatar_url: "/applications/SarcasticChat/Marv.svg",
  background_image_url: "/applications/SarcasticChat/SarcasticChat-bg.png",
  welcome_message: `Hello, I'm Lawrence McDaniel, an adaptive chatbot. I use natural language processing to adapt myself to your prompts. I also leverage OpenAI API 'Function Calling.' If you ask about Lawrence McDaniel then I'll turn into one heck of a shameless promotor on my own behalf. Otherwise, I'll behave like a regular chatbot.`,
  example_prompts: [
    '"In what year was William Shakespear 25 years old?"',
    '"Is Lawrence McDaniel a web developer?"',
    '"what is a good roast chicken recipe?"',
    '"Is Lawrence McDaniel a good citizen?"',
    '"Are Lawrence McDaniel and Chuck Norris friends?"',
  ],
  placeholder_text: `ask me anything about .... me!`,
  info_url: OPENAI_EXAMPLES_URL + SLUG,
  file_attach_button: false,
  uses_openai: true,
  uses_openai_api: false,
  uses_langchain: true,
  uses_memory: true,
};

export default FunctionCalling;
