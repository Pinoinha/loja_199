import React from 'react';
import ReactDOM from 'react-dom/client';
import {Link} from 'react-router-dom';
import './index.css';

export default class Button extends React.Component{
    

    render(){
        let link;
        if (this.props.link == null){
            link = <>{this.props.value}</>;
        } else{
            link = <Link to={this.props.link}>{this.props.value}</Link>;
        }
        return(
          <button className='back-button' onClick={this.props.clickFunc} type={this.props.type}> 
            {link}
          </button>  
        )
    }
}