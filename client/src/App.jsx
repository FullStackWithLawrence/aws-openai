// see: https://www.npmjs.com/package/react-pro-sidebar
import { useState, useEffect } from 'react';
import './App.css';
import ChatApp from './components/chatApp/Component';
import { Sidebar, Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import { ContainerLayout, SidebarLayout, ContentLayout, Logo } from './components/Layout/';
import { FaInfo, FaBookOpen, FaDatabase, FaYoutube, FaGithub, FaLinkedin, FaBrush, FaCode } from "react-icons/fa";
import { APPLICATIONS } from './config';

import AeroAssist from './applications/AeroAssist';
import CodeExplainer from './applications/CodeExplainer';
import CodeImprovement from './applications/CodeImprovement';
import CSVify from './applications/CSVify';
import Emojibot from './applications/Emojibot';
import Emojibot4 from './applications/Emojibot4';
import English2French from './applications/English2French';
import FunctionCreator from './applications/FunctionCreator';
import GrammarGenius from './applications/GrammarGenius';
import InterviewQuestions from './applications/InterviewQuestions';
import KeyWords from './applications/KeyWords';
import KidsDigest from './applications/KidsDigest';
import LessonPlanWriter from './applications/LessonPlanWriter';
import MeetingNotesSummarizer from './applications/MeetingNotesSummarizer';
import Mood2CSSColor from './applications/Mood2CSSColor';
import MemoWriter from './applications/MemoWriter';
import ProductNameGenerator from './applications/ProductNameGenerator';
import ProConDiscusser from './applications/ProConDiscusser';
import PythonDebugger from './applications/PythonDebugger';
import RapBattle from './applications/RapBattle';
import ReviewClassifier from './applications/ReviewClassifier';
import SarcasticChat from './applications/SarcasticChat';
import SinglePageWebapp from './applications/SinglePageWebapp';
import SocraticTutor from './applications/SocraticTutor';
import SpreadsheetGenerator from './applications/SpreadsheetGenerator';
import SqlTranslator from './applications/SqlTranslator';
import TimeComplexity from './applications/TimeComplexity';
import TweetClassifier from './applications/TweetClassifier';
import TurnByTurnDirections from './applications/TurnByTurnDirections';
import VRFitness from './applications/VRFitness';

const currentYear = new Date().getFullYear();

const Footer = () => {
  return (
    <div className='footer'>
      <p>© {currentYear} <a href='https://lawrencemcdaniel.com'>Lawrence McDaniel</a> | <a href='https://openai.com/'><img src='openai-logo.svg' /> OpenAI Python API</a> | <a href='https://react.dev/'><img src='../public/react-logo.svg' /> React</a> | <a href='https://aws.amazon.com/'><img src='../public/aws-logo.svg' /> Amazon Web Services</a> | <a href='https://www.terraform.io/'><img src='terraform-logo.svg' /> Terraform</a> | <a href='https://github.com/FullStackWithLawrence/aws-openai' target='_blank'><img src='../public/github-logo.svg' /> Source code</a></p>
    </div>
  );
};

const App = () => {
  const [selectedItem, setSelectedItem] = useState(APPLICATIONS.RapBattle);

  const handleItemClick = (item) => {
    setSelectedItem(item);
  };
  return (
    <div className='App'>
      <h1 className='app-title'>OpenAI Code Samples</h1>
      <ContainerLayout>
        <SidebarLayout>
          <div style={{ display: 'flex',
                        height: '100%',
                        minHeight: '400px'
                      }}>
            <Sidebar backgroundColor='#1d5268'>
              <Menu menuItemStyles={{
                      button: ({ level, active, disabled }) => {
                          // only apply styles on first level elements of the tree
                          if (level === 0)
                            return {
                              color: disabled ? 'gray' : 'lightgray',
                              backgroundColor: active ? '#eecef9' : undefined,
                            };
                        },
                      }}
              >
                <a href='https://openai.com/' target='_blank'>
                  <img src='../public/OpenAI_Logo.png' alt='OpenAI Logo' className='app-logo' style={{ position: 'absolute', top: 0, left: 0 }} />
                </a>
                <h5 className='sample-applications'>Sample Applications</h5>
                <SubMenu label='Fun Apps' defaultOpen icon={<FaBrush />}>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.RapBattle)}>Rap Battle</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.SocraticTutor)}>Socratic Tutor</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.ProConDiscusser)}>Pros and Cons</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.SarcasticChat)}>Sarcastic Chatbot</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.Emojibot4)}>Emoji ChatBot</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.TweetClassifier)}>Tweet Classifier</MenuItem>
                </SubMenu>
                <SubMenu label='Personal Assistant' icon={<FaBrush />}>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.VRFitness)}>VR Fitness Designer</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.GrammarGenius)}>Grammar Genius</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.English2French)}>French Translator</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.TurnByTurnDirections)}>Personal Navigator</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.KidsDigest)}>Kids Digest</MenuItem>
                </SubMenu>
                <SubMenu label="Office Productivity" icon={<FaBookOpen />}>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.AeroAssist)}>Aero Assist</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.KeyWords)}>Keyword Generator</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.InterviewQuestions)}>Interview Assistant</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.MemoWriter)}>Memo Writer</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.LessonPlanWriter)}>Lesson Plan Writer</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.MeetingNotesSummarizer)}>Meeting Summarizer</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.ProductNameGenerator)}>Product Name Generator</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.ReviewClassifier)}>Product Review Classifier</MenuItem>
                </SubMenu>
                <SubMenu label='Data Apps' icon={<FaDatabase />}>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.CSVify)}>CSVify</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.SpreadsheetGenerator)}>Spreadsheet Generator</MenuItem>
                </SubMenu>
                <SubMenu label='Coding Apps' icon={<FaCode />}>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.FunctionCreator)}>Function Creator</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.TimeComplexity)}>Time Complexity</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.CodeExplainer)}>Code Explainer</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.PythonDebugger)}>Python Debugger</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.SqlTranslator)}>SQL Translator</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.CodeImprovement)}>Coding CoPilot</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.Mood2CSSColor)}>Mood to CSS Color</MenuItem>
                  <MenuItem onClick={() => handleItemClick(APPLICATIONS.SinglePageWebapp)}>SPA Scaffolder</MenuItem>
                </SubMenu>
                <h5>More</h5>
                <MenuItem icon={<FaInfo />}>About Me</MenuItem>
                <MenuItem icon={<FaLinkedin />}>LinkedIn</MenuItem>
                <MenuItem icon={<FaYoutube />}>YouTube video</MenuItem>
                <MenuItem icon={<FaGithub />}>GitHub</MenuItem>
              </Menu>
              {/* <a href='https://www.youtube.com/@FullStackWithLawrence' target="_blank">
                <Logo alt="Logo" />
              </a> */}
            </Sidebar>
          </div>
        </SidebarLayout>
        <ContentLayout>
          {selectedItem === APPLICATIONS.AeroAssist && <ChatApp {...AeroAssist} />}
          {selectedItem === APPLICATIONS.CodeExplainer && <ChatApp {...CodeExplainer} />}
          {selectedItem === APPLICATIONS.CodeImprovement && <ChatApp {...CodeImprovement} />}
          {selectedItem === APPLICATIONS.CSVify && <ChatApp {...CSVify} />}
          {selectedItem === APPLICATIONS.Emojibot && <ChatApp {...Emojibot} />}
          {selectedItem === APPLICATIONS.Emojibot4 && <ChatApp {...Emojibot4} />}
          {selectedItem === APPLICATIONS.English2French && <ChatApp {...English2French} />}
          {selectedItem === APPLICATIONS.FunctionCreator && <ChatApp {...FunctionCreator} />}
          {selectedItem === APPLICATIONS.GrammarGenius && <ChatApp {...GrammarGenius} />}
          {selectedItem === APPLICATIONS.InterviewQuestions && <ChatApp {...InterviewQuestions} />}
          {selectedItem === APPLICATIONS.KeyWords && <ChatApp {...KeyWords} />}
          {selectedItem === APPLICATIONS.KidsDigest && <ChatApp {...KidsDigest} />}
          {selectedItem === APPLICATIONS.LessonPlanWriter && <ChatApp {...LessonPlanWriter} />}
          {selectedItem === APPLICATIONS.MeetingNotesSummarizer && <ChatApp {...MeetingNotesSummarizer} />}
          {selectedItem === APPLICATIONS.Mood2CSSColor && <ChatApp {...Mood2CSSColor} />}
          {selectedItem === APPLICATIONS.MemoWriter && <ChatApp {...MemoWriter} />}
          {selectedItem === APPLICATIONS.ProductNameGenerator && <ChatApp {...ProductNameGenerator} />}
          {selectedItem === APPLICATIONS.ProConDiscusser && <ChatApp {...ProConDiscusser} />}
          {selectedItem === APPLICATIONS.PythonDebugger && <ChatApp {...PythonDebugger} />}
          {selectedItem === APPLICATIONS.RapBattle && <ChatApp {...RapBattle} />}
          {selectedItem === APPLICATIONS.ReviewClassifier && <ChatApp {...ReviewClassifier} />}
          {selectedItem === APPLICATIONS.SarcasticChat && <ChatApp {...SarcasticChat} />}
          {selectedItem === APPLICATIONS.SinglePageWebapp && <ChatApp {...SinglePageWebapp} />}
          {selectedItem === APPLICATIONS.SocraticTutor && <ChatApp {...SocraticTutor} />}
          {selectedItem === APPLICATIONS.SpreadsheetGenerator && <ChatApp {...SpreadsheetGenerator} />}
          {selectedItem === APPLICATIONS.SqlTranslator && <ChatApp {...SqlTranslator} />}
          {selectedItem === APPLICATIONS.TimeComplexity && <ChatApp {...TimeComplexity} />}
          {selectedItem === APPLICATIONS.TweetClassifier && <ChatApp {...TweetClassifier} />}
          {selectedItem === APPLICATIONS.TurnByTurnDirections && <ChatApp {...TurnByTurnDirections} />}
          {selectedItem === APPLICATIONS.VRFitness && <ChatApp {...VRFitness} />}
        </ContentLayout>
      </ContainerLayout>
      <Footer />
    </div>
  )
}

export default App;
