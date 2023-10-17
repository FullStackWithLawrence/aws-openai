
import React from 'react';
import { useState } from 'react';
import ReactModal from 'react-modal';

import './Component.css';

export function ErrorDialog(props) {
  const isModalOpen = props.isModalOpen;
  const modalTitle = props.title;
  const modalMessage = props.message;
  const closeChatModal = props.onCloseClick;
  return (
    <ChatModal isModalOpen={isModalOpen} title={modalTitle} message={modalMessage} onCloseClick={closeChatModal} />
  );
}

export function ChatModal(props) {

  const ModalStyle = {
    overlay: {
      backgroundColor: 'rgba(0, 0, 0, 0.5)',
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      zIndex: 9999 // set a high z-index value
    },
    content: {
      margin: 'auto',
      width: '50%',
      height: '25%',
      backgroundColor: 'white',
      zIndex: 10000 // set an even higher z-index value
    }
  };
  return (
    <ReactModal
      isOpen={props.isModalOpen}
      onRequestClose={props.onCloseClick}
      appElement={document.getElementById('root')}
      style={ModalStyle}
      >
        <div className='modal'>
          <h2>{props.title}</h2>
          <p>{props.message}</p>
          <button className="modal-button" onClick={props.onCloseClick}>Close</button>
        </div>
    </ReactModal>
  );
}
