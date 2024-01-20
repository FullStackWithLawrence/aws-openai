import React from "react";
import ReactModal from "react-modal";
import PropTypes from "prop-types";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faExclamation } from "@fortawesome/free-solid-svg-icons";

import "./Modal.css";

export function ChatModal(props) {
  const ModalStyle = {
    overlay: {
      backgroundColor: "rgba(0, 0, 0, 0.5)",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      zIndex: 9999, // set a high z-index value
    },
    content: {
      margin: "auto",
      width: "50%",
      height: "25%",
      backgroundColor: "white",
      zIndex: 10000, // set an even higher z-index value
    },
  };
  return (
    <ReactModal
      isOpen={props.isModalOpen}
      onRequestClose={props.onCloseClick}
      appElement={document.getElementById("root")}
      style={ModalStyle}
    >
      <div className="modal-container">
        <div className="modal">
          <div className="modal-header">
            <FontAwesomeIcon icon={faExclamation} className="modal-icon" />
            <h2>{props.title}</h2>
            <hr />
          </div>
          <p>{String(props.message)}</p>
          <button className="modal-button" onClick={props.onCloseClick}>
            Close
          </button>
        </div>
      </div>
    </ReactModal>
  );
}

ChatModal.propTypes = {
  isModalOpen: PropTypes.bool.isRequired,
  onCloseClick: PropTypes.func.isRequired,
  title: PropTypes.string.isRequired,
  message: PropTypes.string.isRequired,
};
