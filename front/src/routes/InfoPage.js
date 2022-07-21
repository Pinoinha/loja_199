import React, { Component } from "react";
import '../components/index.css';
import Axios from 'axios';
import PresencaForm from '../components/presencaForm.js';
import baseUrl from '../components/baseUrl.js';
import axios from "axios";

let objeto = {id: -4, nome: 'Placeholder',data:'20-06-2022', preco: '0,00', valor: '0,00', matricula: -1, produtos: [{id:-2,quantidade:3},{id:-3, quantidade:2}]};
export default class FormPage extends React.Component{
    state = {
        card: []
    }
    
    marcaPresenca(){
        //HandlePresenca
        const targetUrl = baseUrl + 'presenca'
        let envioPresenca = {}
        envioPresenca.matricula = objeto.matricula
        envioPresenca.condicao = 0
        axios.post(targetUrl, envioPresenca)
    }

    componentDidMount(){
        console.log(window.location.pathname)
        const path = window.location.pathname
        const arg1 = path.split('/')[path.split('/').length-1]
        const targetUrl = baseUrl + this.props.value
        this.setState({targetUrl})
        //console.log(targetUrl)
        // ADEQUAR PARA API
        Axios.get(targetUrl).then((response)=>{
            // console.log(response.data.cards[0])
            // const card = response.data.cards[0]
            // this.setState({card})
            // console.log(this.state.card)
            objeto = (this.props.value === "colaborador" ?response.filter(objeto.matricula === arg1) : response.filter(objeto.id === arg1));
            
          }).then(console.log())
      } 
    render(){
        let content = <></>;

        switch (this.props.value){
            case "venda":
                content = (<div>
                    <ul>
                        <li>
                            ID: {objeto.id}
                        </li>
                        <li>
                            Data: {objeto.data}
                        </li>
                        <li>
                            Valor: {objeto.valor}
                        </li>
                        <li>
                            Responsável: {objeto.matricula === undefined ? 'null' : objeto.matricula}
                        </li>
                        <li> Produtos
                        <ul>
                        {objeto.produtos !== undefined ?
                        objeto.produtos.map( produto => (
                            <li> ID: {produto.id} | {produto.quantidade} unidades</li>
                        )) : 
                        <li>null</li>}
                        </ul>
                        </li>
                    </ul>
                </div>)
                break;
            case "colaborador":
                content = (<div>
                    <ul>
                        <li>
                            Nome: {objeto.nome}
                        </li>
                        <li>
                            Matrícula: {objeto.matricula}
                        </li>
                        <li>
                            Presente?
                        </li>
                    </ul>
                    <PresencaForm clickFunc = {this.marcaPresenca} value="Marcar Presença"/>
                </div>)
                break;
            case "produto":
                content = (<div>
                    <ul>
                        <li>
                            ID: {objeto.id}
                        </li>
                        <li>
                            nome: {objeto.nome}
                        </li>
                        <li>
                            preco: {objeto.preco}
                        </li>
                    </ul>
                </div>)
                break;
            default:
                console.log("Como?")
        }
        return(
            <div>
                {content}
            </div>
        )
    }
}