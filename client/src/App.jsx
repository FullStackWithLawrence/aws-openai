// React code
import React from "react";
import { useState } from "react";

// Third party components
import { Sidebar, Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import {
  ContainerLayout,
  SidebarLayout,
  ContentLayout,
  Logo,
} from "./components/Layout/";
import {
  FaInfo,
  FaDatabase,
  FaCode,
  FaChartLine,
  FaClipboardList,
  FaGamepad,
} from "react-icons/fa";

// Our code
import "./App.css";
import ChatApp from "./components/chatApp/Component";
import AboutPage from "./components/about/Component";
import { APPLICATIONS } from "./config";

// chatApp definitions
import AeroAssist from "./applications/AeroAssist";
import CodeExplainer from "./applications/CodeExplainer";
import CodeImprovement from "./applications/CodeImprovement";
import CSVify from "./applications/CSVify";
import Emojibot from "./applications/Emojibot";
import Emojibot4 from "./applications/Emojibot4";
import English2French from "./applications/English2French";
import FunctionCreator from "./applications/FunctionCreator";
import FunctionCalling from "./applications/FunctionCalling";
import GrammarGenius from "./applications/GrammarGenius";
import InterviewQuestions from "./applications/InterviewQuestions";
import KeyWords from "./applications/KeyWords";
import KidsDigest from "./applications/KidsDigest";
import LessonPlanWriter from "./applications/LessonPlanWriter";
import MeetingNotesSummarizer from "./applications/MeetingNotesSummarizer";
import Mood2CSSColor from "./applications/Mood2CSSColor";
import MemoWriter from "./applications/MemoWriter";
import ProductNameGenerator from "./applications/ProductNameGenerator";
import ProConDiscusser from "./applications/ProConDiscusser";
import PythonDebugger from "./applications/PythonDebugger";
import RapBattle from "./applications/RapBattle";
import ReviewClassifier from "./applications/ReviewClassifier";
import SarcasticChat from "./applications/SarcasticChat";
import SinglePageWebapp from "./applications/SinglePageWebapp";
import SocraticTutor from "./applications/SocraticTutor";
import SpreadsheetGenerator from "./applications/SpreadsheetGenerator";
import SqlTranslator from "./applications/SqlTranslator";
import TimeComplexity from "./applications/TimeComplexity";
import TweetClassifier from "./applications/TweetClassifier";
import TurnByTurnDirections from "./applications/TurnByTurnDirections";
import VRFitness from "./applications/VRFitness";

const currentYear = new Date().getFullYear();

const Footer = () => {
  return (
    <div className="footer hide-small">
      <p>
        © {currentYear}{" "}
        <a href="https://lawrencemcdaniel.com">lawrencemcdaniel.com</a> |{" "}
        <a href="https://openai.com/">
          <img src="openai-logo.svg" /> OpenAI Python API
        </a>{" "}
        |{" "}
        <a href="https://react.dev/">
          <img src="/react-logo.svg" /> React
        </a>{" "}
        |{" "}
        <a href="https://aws.amazon.com/">
          <img src="/aws-logo.svg" />
        </a>{" "}
        |{" "}
        <a href="https://www.terraform.io/">
          <img src="terraform-logo.svg" /> Terraform
        </a>{" "}
        |{" "}
        <a
          href="https://github.com/FullStackWithLawrence/aws-openai"
          target="_blank"
          rel="noreferrer"
        >
          <img src="/github-logo.svg" /> Source code
        </a>
      </p>
    </div>
  );
};

const App = () => {
  const [selectedItem, setSelectedItem] = useState(
    APPLICATIONS.FunctionCalling,
  );

  const handleItemClick = (item) => {
    setSelectedItem(item);
  };
  return (
    <div className="App">
      <h1 className="app-title hide-small">OpenAI Code Samples</h1>
      <ContainerLayout>
        <SidebarLayout className="hide-small">
          <div style={{ display: "flex", height: "100%", minHeight: "400px" }}>
            <Sidebar backgroundColor="#1d5268">
              <Menu
                menuItemStyles={{
                  button: ({ level, active, disabled }) => {
                    // only apply styles on first level elements of the tree
                    if (level === 0)
                      return {
                        color: disabled ? "gray" : "lightgray",
                        backgroundColor: active ? "#eecef9" : undefined,
                      };
                  },
                }}
              >
                <a href="https://openai.com/" target="_blank" rel="noreferrer">
                  <img
                    src="/OpenAI_Logo.png"
                    alt="OpenAI Logo"
                    className="app-logo"
                    style={{ position: "absolute", top: 0, left: 0 }}
                  />
                </a>
                <h5 className="sample-applications">Sample Applications</h5>
                <SubMenu label="Fun Apps" defaultOpen icon={<FaGamepad />}>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.SarcasticChat)}
                  >
                    {SarcasticChat.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.FunctionCalling)
                    }
                  >
                    {FunctionCalling.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.Emojibot)}
                  >
                    {Emojibot.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.Emojibot4)}
                  >
                    {Emojibot4.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.RapBattle)}
                  >
                    {RapBattle.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.SocraticTutor)}
                  >
                    {SocraticTutor.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.ProConDiscusser)
                    }
                  >
                    {ProConDiscusser.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.TweetClassifier)
                    }
                  >
                    {TweetClassifier.sidebar_title}
                  </MenuItem>
                </SubMenu>
                <SubMenu label="Personal Assistant" icon={<FaClipboardList />}>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.VRFitness)}
                  >
                    {VRFitness.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.GrammarGenius)}
                  >
                    {GrammarGenius.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.English2French)}
                  >
                    {English2French.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.TurnByTurnDirections)
                    }
                  >
                    {TurnByTurnDirections.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.KidsDigest)}
                  >
                    {KidsDigest.sidebar_title}
                  </MenuItem>
                </SubMenu>
                <SubMenu label="Office Productivity" icon={<FaChartLine />}>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.AeroAssist)}
                  >
                    {AeroAssist.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.KeyWords)}
                  >
                    {KeyWords.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.InterviewQuestions)
                    }
                  >
                    {InterviewQuestions.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.MemoWriter)}
                  >
                    {MemoWriter.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.LessonPlanWriter)
                    }
                  >
                    {LessonPlanWriter.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.MeetingNotesSummarizer)
                    }
                  >
                    {MeetingNotesSummarizer.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.ProductNameGenerator)
                    }
                  >
                    {ProductNameGenerator.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.ReviewClassifier)
                    }
                  >
                    {ReviewClassifier.sidebar_title}
                  </MenuItem>
                </SubMenu>
                <SubMenu label="Data Apps" icon={<FaDatabase />}>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.CSVify)}
                  >
                    {CSVify.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.SpreadsheetGenerator)
                    }
                  >
                    {SpreadsheetGenerator.sidebar_title}
                  </MenuItem>
                </SubMenu>
                <SubMenu label="Coding Apps" icon={<FaCode />}>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.FunctionCreator)
                    }
                  >
                    {FunctionCreator.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.TimeComplexity)}
                  >
                    {TimeComplexity.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.CodeExplainer)}
                  >
                    {CodeExplainer.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.PythonDebugger)}
                  >
                    {PythonDebugger.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.SqlTranslator)}
                  >
                    {SqlTranslator.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.CodeImprovement)
                    }
                  >
                    {CodeImprovement.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() => handleItemClick(APPLICATIONS.Mood2CSSColor)}
                  >
                    {Mood2CSSColor.sidebar_title}
                  </MenuItem>
                  <MenuItem
                    onClick={() =>
                      handleItemClick(APPLICATIONS.SinglePageWebapp)
                    }
                  >
                    {SinglePageWebapp.sidebar_title}
                  </MenuItem>
                </SubMenu>
                <hr />
                <MenuItem
                  icon={<FaInfo />}
                  onClick={() => handleItemClick("AboutPage")}
                >
                  About
                </MenuItem>
              </Menu>
            </Sidebar>
          </div>
        </SidebarLayout>
        <ContentLayout>
          {selectedItem === "AboutPage" && <AboutPage />}

          {selectedItem === APPLICATIONS.AeroAssist && (
            <ChatApp {...AeroAssist} />
          )}
          {selectedItem === APPLICATIONS.CodeExplainer && (
            <ChatApp {...CodeExplainer} />
          )}
          {selectedItem === APPLICATIONS.CodeImprovement && (
            <ChatApp {...CodeImprovement} />
          )}
          {selectedItem === APPLICATIONS.CSVify && <ChatApp {...CSVify} />}
          {selectedItem === APPLICATIONS.Emojibot && <ChatApp {...Emojibot} />}
          {selectedItem === APPLICATIONS.Emojibot4 && (
            <ChatApp {...Emojibot4} />
          )}
          {selectedItem === APPLICATIONS.English2French && (
            <ChatApp {...English2French} />
          )}
          {selectedItem === APPLICATIONS.FunctionCreator && (
            <ChatApp {...FunctionCreator} />
          )}
          {selectedItem === APPLICATIONS.GrammarGenius && (
            <ChatApp {...GrammarGenius} />
          )}
          {selectedItem === APPLICATIONS.InterviewQuestions && (
            <ChatApp {...InterviewQuestions} />
          )}
          {selectedItem === APPLICATIONS.KeyWords && <ChatApp {...KeyWords} />}
          {selectedItem === APPLICATIONS.KidsDigest && (
            <ChatApp {...KidsDigest} />
          )}
          {selectedItem === APPLICATIONS.LessonPlanWriter && (
            <ChatApp {...LessonPlanWriter} />
          )}
          {selectedItem === APPLICATIONS.MeetingNotesSummarizer && (
            <ChatApp {...MeetingNotesSummarizer} />
          )}
          {selectedItem === APPLICATIONS.Mood2CSSColor && (
            <ChatApp {...Mood2CSSColor} />
          )}
          {selectedItem === APPLICATIONS.MemoWriter && (
            <ChatApp {...MemoWriter} />
          )}
          {selectedItem === APPLICATIONS.ProductNameGenerator && (
            <ChatApp {...ProductNameGenerator} />
          )}
          {selectedItem === APPLICATIONS.ProConDiscusser && (
            <ChatApp {...ProConDiscusser} />
          )}
          {selectedItem === APPLICATIONS.PythonDebugger && (
            <ChatApp {...PythonDebugger} />
          )}
          {selectedItem === APPLICATIONS.RapBattle && (
            <ChatApp {...RapBattle} />
          )}
          {selectedItem === APPLICATIONS.ReviewClassifier && (
            <ChatApp {...ReviewClassifier} />
          )}
          {selectedItem === APPLICATIONS.SarcasticChat && (
            <ChatApp {...SarcasticChat} />
          )}
          {selectedItem === APPLICATIONS.FunctionCalling && (
            <ChatApp {...FunctionCalling} />
          )}
          {selectedItem === APPLICATIONS.SinglePageWebapp && (
            <ChatApp {...SinglePageWebapp} />
          )}
          {selectedItem === APPLICATIONS.SocraticTutor && (
            <ChatApp {...SocraticTutor} />
          )}
          {selectedItem === APPLICATIONS.SpreadsheetGenerator && (
            <ChatApp {...SpreadsheetGenerator} />
          )}
          {selectedItem === APPLICATIONS.SqlTranslator && (
            <ChatApp {...SqlTranslator} />
          )}
          {selectedItem === APPLICATIONS.TimeComplexity && (
            <ChatApp {...TimeComplexity} />
          )}
          {selectedItem === APPLICATIONS.TweetClassifier && (
            <ChatApp {...TweetClassifier} />
          )}
          {selectedItem === APPLICATIONS.TurnByTurnDirections && (
            <ChatApp {...TurnByTurnDirections} />
          )}
          {selectedItem === APPLICATIONS.VRFitness && (
            <ChatApp {...VRFitness} />
          )}
        </ContentLayout>
      </ContainerLayout>
      <Footer />
    </div>
  );
};

export default App;
