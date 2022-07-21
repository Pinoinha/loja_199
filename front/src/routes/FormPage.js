import React from "react";
import '../components/index.css';
//import Header from '../components/header.js';
//import Button from '../components/button.js';
import Axios from "axios";
import  baseUrl from '../components/baseUrl.js';

let envio = {nome:'a', preco:0.00};
let produtosEnvio = [];
let produtoEnvio = {nome:'',idProduto:0,preco:0};
let produtosP = []; // Produtos vindos do GET
export default class FormPage extends React.Component{
    state = {
        fields:[],
        venda : {idVenda:0,
                 dataVenda:0,
                 valor:0,
                 matricula:0,
                 idQtdProdutos:{
                 }
                },
        produto: {id:0,
                  nome:'',
                  preco:0},
        countProdutos: 0,
        produtosPossiveis:[]
    }
    
    handleFieldChange = (event,id) => {
        switch(this.props.value){
            case 'venda':
                switch(id){
                    case 0:
                        envio.idVenda = event.target.value
                        break;
                    case 1:
                        envio.dataVenda = event.target.value
                        break;
                    case 2:
                        envio.valorTotal = event.target.value
                        break;
                    case 3:
                        envio.matricula = event.target.value
                        break;
                    case 4:
                        //console.log(event.target);
                        
                        produtoEnvio.id = event.target.value
                        break;
                    case 5:
                        produtoEnvio.quantidade = event.target.value
                        break;
                    case 6:
                        if (produtoEnvio !== {}){
                            // const objEnvio = {
                            //     produtoEnvio.id : produtoEnvio.qtd
                            // }
                            const id = produtoEnvio.id
                            const qtd = produtoEnvio.quantidade
                            //produtosEnvio.id = qtd
                            produtosEnvio[id] = qtd
                            //produtosEnvio.push(produtoEnvio);
                        }
                        console.log(produtosEnvio)
                        produtoEnvio = {};
                        break;
                    default:
                        console.log("Você não deveria estar aqui...");
                        break;
                }
                break;
            case 'produto':
                switch(id){
                    case 0:
                        envio.idProduto = event.target.value
                        console.log(this.state)
                        break;
                    case 1:
                        envio.nome = event.target.value
                        break;
                    case 2:
                        envio.preco = event.target.value
                        break;
                    default:
                        console.log("Você não deveria estar aqui...");
                        break;
                }
                break;
            default:
                console.log("Você não deveria estar aqui...");
                break;
        };
    }
   

    handleSubmit = event =>{
        event.preventDefault();
        
        
        switch(this.props.value){
            case 'venda':
                envio.produtos = produtosEnvio
                Axios.post(
                    this.state.url,
                    {envio}
                ).then( response =>{
                    console.log(envio)
                    console.log(response)
                })
                break;
            case 'produto':
                console.log(produtoEnvio)
                Axios.post(
                    this.state.url,
                    {nome : envio.nome,
                     preco : envio.preco}
                ).then( response =>{
                    console.log(produtoEnvio);
                    console.log(response)
                })
                break;
            default:
                console.log("Você não deveria estar aqui...");
                break;
        }

        switch(this.props.value){
            case 'venda':
                console.log(envio)
                break;
            case 'produto':
                console.log(envio)
                break;
            default:
                console.log("Você não deveria estar aqui...");
                break;
        }
        
    }
    componentDidMount(){
        if (this.props.value === "venda"){
            
            this.setState({url: baseUrl + 'venda'})
            const produtoUrl = baseUrl + 'produto'
            Axios.get(produtoUrl, {headers: {
                'ngrok-skip-browser-warning' : 1}}).then(
            //Axios.get('https://api.magicthegathering.io/v1/cards?set=GK1').then(
                (response) => {
                    //const produtos = response.data
                    const produtos = response.data.cards
                    this.setState({produtosPossiveis: produtos})
                    produtosP = produtos
                    this.setState({fields : 
                        <div>
                            {/* {<label >
                            ID: 
                            <input type='number' name='ID' placeholder="00000000" size = '6' onChange={(event) => this.handleFieldChange(event,0)} required/>
                            </label>
                            <br/>} 
                            <label display='flex'>
                            Data da Venda: 
                            <input type='date' name='Data da Venda' onChange={(event) => this.handleFieldChange(event,1)} required/>
                            </label>
                            <br/>*/}
                            <label display='flex'>
                            Valor total: 
                            <input type='number' name='Valor total' placeholder = "00,00" step="0.01" onChange={(event) => this.handleFieldChange(event,2)} required/>
                            </label>
                            <br/>
                            <label display='flex'>
                            Matrícula do vendedor: 
                            <input type='number' name='Matrícula do vendedor' onChange={(event) => this.handleFieldChange(event,3)} required/>
                            </label>
                            <br/>
                            

                            <label>
                                Adicionar produto à venda: 
                                <select id='produtos' name='produtos' size='1' onChange={(event) => this.handleFieldChange(event,4)}required >
                                <option invalid></option>
                                {
                                produtosP.map(produto => (   
                                    
                                        <option value={produto.idProduto} label={produto.nome}>
                                            {produto.nome} | {produto.preco}
                                        </option>
                                        
                                    ))}
                                    {/*<option value={produto.id} label={produto.name}>
                                            {produto.name}
                                        </option>*/}
                                </select>
                                <input id='quantidade' type='number' onChange={(event) => this.handleFieldChange(event,5)}/>
                            <input type='button' name="Adicionar Produto" onClick={(event) => this.handleFieldChange(event,6)} value="+"/>
                            </label>
                        </div>});

                console.log(response)}
                
            )
            
        } else if (this.props.value === "produto"){
            this.setState({fields : 
                <div>
                    {/* <label >
                    ID:
                    <input type='number' name='ID' placeholder="00000000" size = '6' onChange={(event) => this.handleFieldChange(event,0)} required/>
                    </label>
                    <br/> */}
                    <label display='flex'>
                    Nome:
                    <input type='text' name='Nome' placeholder="Leite Condensado Italac 395g" min='1' onChange={(event) => this.handleFieldChange(event,1)} required/>
                    </label>
                    <br/>
                    <label display='flex'>
                    Preço:
                    <input type='number' name='Preço' placeholder="7,50" step='0.01' onChange={(event) => this.handleFieldChange(event,2)} />
                    </label>
                    <br/>
                </div>
            });
            this.setState({url:baseUrl + 'produto'})
        }
    }
    render(){
        return(
            <div>
                {/*REPLACE WITH API STUFF*/}
                Implementar form de criar {this.props.value} aqui.
                <form onSubmit={this.handleSubmit} display='block'>
                    {this.state.fields}
                    {produtosEnvio.map(produtoE => (
                                <div>ID: {produtoE.id} | {produtoE.quantidade} unidades</div>
                            ))}
                    <button type='submit'>Adicionar {this.props.value}</button>
                </form>
            </div>
        )
    }
}