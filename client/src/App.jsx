// see: https://www.npmjs.com/package/react-pro-sidebar
import './App.css';
import ChatApp from './components/chatApp/Component';
import { Sidebar, Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import { ContainerLayout, SidebarLayout, ContentLayout, MenuLayout, Logo } from './components/Layout/';
import { FaCalendar, FaInfo, FaBookOpen, FaLaptopCode, FaDatabase, FaYoutube, FaGithub, FaLinkedin, FaBrush } from "react-icons/fa";
import AeroAssist from './applications/AeroAssist';
import GrammarGenius from './applications/GrammarGenius';
import KidsDigest from './applications/KidsDigest';
import CSVify from './applications/CSVify';
import Emojibot from './applications/Emojibot';
import TimeComplexity from './applications/TimeComplexity';
import CodeExplainer from './applications/CodeExplainer';
import KeyWords from './applications/KeyWords';
import ProductNameGenerator from './applications/ProductNameGenerator';
import PythonDebugger from './applications/PythonDebugger';
import SpreadsheetGenerator from './applications/SpreadsheetGenerator';
import TweetClassifier from './applications/TweetClassifier';

const App = () => {
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
                <SubMenu defaultOpen label="Assistants" icon={<FaBookOpen />}>
                  <MenuItem>Grammar Genius</MenuItem>
                  <MenuItem>Aero Assist</MenuItem>
                  <MenuItem>Kids Digest</MenuItem>
                </SubMenu>
                <SubMenu label='Fun' icon={<FaBrush />}>
                  <MenuItem>Emoji Bot</MenuItem>
                  <MenuItem>Tweet Classifier</MenuItem>
                  <MenuItem>Keyword Generator</MenuItem>
                </SubMenu>
                <SubMenu label='Data' icon={<FaDatabase />}>
                  <MenuItem>CSVify</MenuItem>
                  <MenuItem>Spreadsheet Generator</MenuItem>
                </SubMenu>
                <SubMenu label='Python Coding' icon={<FaLaptopCode />}>
                  <MenuItem>Time Complexity</MenuItem>
                  <MenuItem>Code Explainer</MenuItem>
                  <MenuItem>Python Debugger</MenuItem>
                </SubMenu>
                <h5>More</h5>
                <MenuItem icon={<FaInfo />}>About Me</MenuItem>
                <MenuItem icon={<FaLinkedin />}>LinkedIn</MenuItem>
                <MenuItem icon={<FaYoutube />}>YouTube video</MenuItem>
                <MenuItem icon={<FaGithub />}>GitHub</MenuItem>
                <a href='https://www.youtube.com/@FullStackWithLawrence' target="_blank">
                  <Logo alt="Logo" />
                </a>
              </Menu>
            </Sidebar>
          </div>
        </SidebarLayout>
        <ContentLayout>
          <ChatApp {...TweetClassifier} />
        </ContentLayout>
      </ContainerLayout>
    </div>
  )
}

export default App;
