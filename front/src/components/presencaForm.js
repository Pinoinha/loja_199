import React from 'react';
import ReactDOM from 'react-dom/client';
import {Link} from 'react-router-dom';
import './index.css';
import  baseUrl from '../components/baseUrl.js';

let matricula;
export default class PresencaForm extends React.Component{

    componentDidMount(){
      const path = window.location.pathname
      const arg1 = path.split('/')[path.split('/').length-1]
      const targetUrl = baseUrl + this.props.value
      matricula = arg1
    }

    render(){
        return(
          <button className='back-button'onClick={this.props.clickFunc}> 
            {this.props.value}
          </button>  
        )
    }
}