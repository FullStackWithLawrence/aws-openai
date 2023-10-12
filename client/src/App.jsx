// see: https://www.npmjs.com/package/react-pro-sidebar
import './App.css';
import ChatApp from './components/chatApp/Component';
import { Sidebar, Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import { ContainerLayout, SidebarLayout, ContentLayout, MenuLayout, Logo } from './components/Layout/';
import { FaCalendar, FaInfo, FaBookOpen, FaLaptopCode, FaDatabase } from "react-icons/fa";
import AeroAssist from './applications/AeroAssist';
import GrammarGenius from './applications/GrammarGenius';
import KidsDigest from './applications/KidsDigest';
import CSVify from './applications/CSVify';
import Emojibot from './applications/Emojibot';

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
                <SubMenu defaultOpen label="Chat Bots" icon={<FaBookOpen />}>
                  <MenuItem>Grammar Genius</MenuItem>
                  <MenuItem>Aero Assist</MenuItem>
                  <MenuItem>Kids Digest</MenuItem>
                </SubMenu>
                <SubMenu label='Data' icon={<FaDatabase />}>
                  <MenuItem>CSVify</MenuItem>
                </SubMenu>
                <SubMenu label='Python Coding' icon={<FaLaptopCode />}></SubMenu>
                <SubMenu label='Explainer' icon={<FaCalendar />}></SubMenu>
                <h5>More</h5>
                <MenuItem icon={<FaInfo />}>About</MenuItem>
              </Menu>
              <a href='https://www.youtube.com/@FullStackWithLawrence' target="_blank">
                <Logo alt="Logo" />
              </a>
            </Sidebar>
          </div>
        </SidebarLayout>
        <ContentLayout>
          <ChatApp {...Emojibot} />
        </ContentLayout>
      </ContainerLayout>

    </div>
  )
}

export default App;
