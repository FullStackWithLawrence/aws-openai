
import React from 'react';
import { useState } from 'react';
import ReactModal from 'react-modal';

import './Component.css';

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
      onRequestClose={props.closeChatModal}
      appElement={document.getElementById('root')}
      style={ModalStyle}
      >
        <div className='modal'>
          <h2>Error</h2>
          <p>There was an error processing your request.</p>
          <p>{props.errMessage}</p>
          <button className="modal-button" onClick={props.closeChatModal}>Close</button>
        </div>
    </ReactModal>
  );
}
