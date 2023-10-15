//
//
import React from 'react';
import './Component.css';
const AboutPage = (props) => {

  return(
    <div className='about-page hide-small'>
      <div className='app-stack' >
        <h2>Application Stack</h2>
        <p>React app running on AWS serverless infrastructure integrated to OpenAI Python API.</p>
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
