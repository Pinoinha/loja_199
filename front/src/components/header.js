import React from 'react';
import {Link} from 'react-router-dom';
import './index.css';

export default class Header extends React.Component{
  render() {
    return(
      <div className="header-parent">
        <div className="header">
          <Link to="/">
          <div className="header-logo"
          onClick={()=>console.log("Isso deveria ir pra pagina inicial")}
          alt="Logo">LOGO</div>
          </Link>
        </div>
      </div>
    );
  }
}

