//
//
import React from 'react';
import './Component.css';
const AboutPage = (props) => {

  return(
    <div className='about-page hide-small'>
      <div className='app-stack' >
        <h2>Application Stack</h2>
        <p><a href='https://react.dev/' target='_blank'>React</a>  app made with <a href='https://www.npmjs.com/package/@chatscope/chat-ui-kit-react' target='_blank'>@chatscope/chat-ui-kit-react</a> and <a href='https://www.npmjs.com/package/react-pro-sidebar' target='_blank'>react-pro-sidebar</a> running on <a href='https://aws.amazon.com/' target='_blank'>AWS</a> serverless infrastructure integrated to <a href='https://platform.openai.com/docs/api-reference?lang=python' target='_blank'>OpenAI Python API</a>.</p>
        <a href='https://github.com/FullStackWithLawrence/aws-openai' target="_blank">
          <img src='/app-stack.123.jpeg' />
        </a>
        <div>Get the source code here: <a href='https://github.com/FullStackWithLawrence/aws-openai' target='_blank'>https://github.com/FullStackWithLawrence/aws-openai</a></div>
      </div>
      <hr />
      <a href='https://www.youtube.com/@FullStackWithLawrence' target="_blank">
        <div className='fswl'></div>
      </a>
    </div>

  )
}

export default AboutPage;
