import React, { Component } from "react";
import '../components/index.css';
import Button from '../components/button.js';
import {Link} from "react-router-dom";
import Axios from "axios";
import  baseUrl from '../components/baseUrl.js';
let objetos = [
  {nome : 'Placeholder da Silva',
    matricula :0,
    idProduto: 333,
    idVenda : 213,
    valorTotal: 25.39
  },
  {nome : 'Placeholder dos Santos',
  matricula :1,
  idProduto: 444,
  idVenda : 345,
  valorTotal: 2.00
  },
  {nome : 'Placeholder de Souza',
  matricula :2,
  idVenda: 456,
  idProduto: 666,
  valorTotal: 25.13
    
  }
]
export default class Page extends React.Component {
  state = {
    cards: []
  }
  componentDidMount(){
    // ADEQUAR PARA API
    const targetUrl = baseUrl + this.props.type
    Axios.get(targetUrl, {headers: {
      'ngrok-skip-browser-warning' : 1}}).then((response)=>{
      console.log(response.data)
      /*const cards = response.data.cards
      this.setState({cards})
      console.log(this.state.cards)*/
      console.log(response.data)
      objetos = response.data
    })
  }  
  render(){
        let keyItem
        let itemName
        return (
            
        <div className="page">
          <ul>
          {//REPLACE WITH API STUFF
          objetos.map(item =>(
            <>
              <div className= 'hide'>
                {keyItem = this.props.type === "colaborador" ? item.matricula : (this.props.type==='venda' ? item.idVenda : item.idProduto)}
                {itemName = (this.props.type === 'colaborador' || this.props.type === 'produto') ? item.nome : item.valorTotal}
              </div>
              
              {//<li key={this.props.type === "colaborador" ? item.matricula : item.id}>
              }
              <li key={keyItem}>  
                <Link to={'id/'+keyItem} >{itemName} | {keyItem}</Link>
              </li>    
            </>
            ))}
            
          </ul>
          
        </div>
    );
  }
}

/*

          <Button value="Vendas"
          clickFunc={() => console.log("Ir para Vendas")}
          state="on"/>
          <Button value="Produtos"
          clickFunc = {() => console.log("Ir para Produtos")}
          state="on"/>

          <Colaboradores state={pageState === "colaboradores" ? "on" : "off"}/>
*/