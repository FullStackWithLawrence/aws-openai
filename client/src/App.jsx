import './App.css';
import ChatApp from './components/chatApp/Component';
import appAeroAssist from './components/appAeroAssist';

const App = () => {
  return (
    <div className='App'>
      <ChatApp {...appAeroAssist} />
    </div>
  )
}

export default App;
