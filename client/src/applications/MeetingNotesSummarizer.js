// see https://github.com/FullStackWithLawrence/aws-openai/blob/main/api/terraform/apigateway_endpoints.tf#L19

import { BACKEND_API_URL, AWS_API_GATEWAY_KEY } from "../config";

const MeetingNotesSummarizer = {
  api_url: BACKEND_API_URL + 'default-meeting-notes-summarizer',
  api_key: AWS_API_GATEWAY_KEY,
  app_name: "Meeting Notes Summarizer",
  assistant_name: "Bodhi",
  avatar_url: '/applications/MeetingNotesSummarizer/Bodhi.svg',
  background_image_url: '/applications/MeetingNotesSummarizer/MeetingNotesSummarizer-bg.svg',
  welcome_message: `Hello, I'm Bodhi, an executive assistant. I can help you summarize meeting notes.`,
  example_prompts: [],
  placeholder_text: `paste your notes for Bodhi...`,
};

export default MeetingNotesSummarizer;
