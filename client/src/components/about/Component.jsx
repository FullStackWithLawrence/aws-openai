//
//
import React from "react";
import "./Component.css";
const AboutPage = () => {
  return (
    <div className="about-page">
      <div className="app-stack">
        <h2>Application Stack</h2>
        <p>
          This application implements each of the{" "}
          <a
            href="https://platform.openai.com/examples"
            target="_blank"
            rel="noreferrer"
          >
            30 Code Samples
          </a>{" "}
          as found in the OpenAI API official documentation. Created with{" "}
          <a href="https://react.dev/" target="_blank" rel="noreferrer">
            React
          </a>{" "}
          leveraging{" "}
          <a
            href="https://www.npmjs.com/package/@chatscope/chat-ui-kit-react"
            target="_blank"
            rel="noreferrer"
          >
            @chatscope/chat-ui-kit-react
          </a>{" "}
          and{" "}
          <a
            href="https://www.npmjs.com/package/react-pro-sidebar"
            target="_blank"
            rel="noreferrer"
          >
            react-pro-sidebar
          </a>{" "}
          running on{" "}
          <a href="https://aws.amazon.com/" target="_blank" rel="noreferrer">
            AWS
          </a>{" "}
          serverless infrastructure integrated to{" "}
          <a
            href="https://platform.openai.com/docs/api-reference?lang=python"
            target="_blank"
            rel="noreferrer"
          >
            OpenAI Python API
          </a>
          .
        </p>
        <a
          href="https://github.com/FullStackWithLawrence/aws-openai"
          target="_blank"
          rel="noreferrer"
        >
          <img src="/app-stack.123.jpeg" />
        </a>
        <div>
          Get the source code here:{" "}
          <a
            href="https://github.com/FullStackWithLawrence/aws-openai"
            target="_blank"
            rel="noreferrer"
          >
            https://github.com/FullStackWithLawrence/aws-openai
          </a>
        </div>
      </div>
      <hr />
      <a
        href="https://www.youtube.com/@FullStackWithLawrence"
        target="_blank"
        rel="noreferrer"
      >
        <div className="fswl"></div>
      </a>
    </div>
  );
};

export default AboutPage;
