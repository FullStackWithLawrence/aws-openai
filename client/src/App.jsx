// see: https://www.npmjs.com/package/react-pro-sidebar
import './App.css';
import ChatApp from './components/chatApp/Component';
import appAeroAssist from './components/appAeroAssist';
import { Sidebar, Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import { ContainerLayout, SidebarLayout, ContentLayout, MenuLayout, Logo } from './components/Layout/';
import { FaBeer, FaCalculator, FaCalendar, FaDochub, FaBookOpen } from "react-icons/fa";

const App = () => {
  return (
    <div className='App'>
      <ContainerLayout>
        <SidebarLayout>
          <div style={{ display: 'flex',
                        height: '100%',
                        minHeight: '400px'
                      }}>
            <Sidebar backgroundColor='#333'>
              <Menu menuItemStyles={{
                      button: ({ level, active, disabled }) => {
                          // only apply styles on first level elements of the tree
                          if (level === 0)
                            return {
                              color: disabled ? '#ffb13e' : '#ffb13e',
                              backgroundColor: active ? '#eecef9' : undefined,
                            };
                        },
                      }}
              >
                <SubMenu defaultOpen label="Charts" icon={<FaBookOpen />}>
                  <MenuItem> Pie charts </MenuItem>
                  <MenuItem> Line charts </MenuItem>
                </SubMenu>
                <MenuItem icon={<FaDochub />}> Documentation </MenuItem>
                <MenuItem icon={<FaCalendar />}> Calendar </MenuItem>
              </Menu>
              <Logo alt="Logo" />
            </Sidebar>
          </div>
        </SidebarLayout>
        <ContentLayout>
          <ChatApp {...appAeroAssist} />
        </ContentLayout>
      </ContainerLayout>

    </div>
  )
}

export default App;
