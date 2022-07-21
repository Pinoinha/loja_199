import React from 'react';
import ReactDOM from 'react-dom/client';
import {Link, Navigate} from 'react-router-dom';
import Axios from 'axios'
import Button from '../components/button.js';
import './index.css';

let confirmacao = <div></div>;
let objeto = {nome: 'Placeholder', id: -4, preco: '0,00', data: '05/06/2022', valor: '0,00', matricula: -1};
let envio;

export default class UpdateForm extends React.Component{
    state = {
        confirmacao:<></>,
        redirect:<></>,
        targetUrl:'',
        card:[]
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
                        envio.valor = event.target.value
                        break;
                    case 3:
                        envio.matricula = event.target.value
                        break;

                    default:
                        console.log("Você não deveria estar aqui...");
                        break;
                }
                break;
            case 'produto':
                switch(id){
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
    //HTTP POST
    handleSubmit = event =>{
        event.preventDefault();
        console.log(window.location.pathname);
        const post = {
            Name: this.state.postName,
            Age:  this.state.postAge
        };
        // REPLACE WITH API STUFF
        Axios.post(
                this.state.targetUrl, 
                {envio}
            ).then( response => {
                console.log(post)
                console.log(response);
                
            }).catch(
                error => {
                    console.log("ERRO!");
                    console.log(error);
                }
            )
    }
    
    componentDidMount(){
        const path = window.location.pathname
        const arg1 = this.props.value
        let TargetUrl = '/api/'+arg1
        this.setState({targetUrl : TargetUrl})
        console.log(TargetUrl)

        Axios.get(TargetUrl).then((response)=>{
            /*console.log(response.data.cards[0])
            const card = response.data.cards[0]
            this.setState({card})
            console.log(this.state.card)*/
            objeto = (this.props.value === "colaborador" ?response.filter(objeto.matricula === arg1) : response.filter(objeto.id === arg1));
            envio = objeto
          })
      }

    // HTTP DELETE
    confirmaDelete = () => {
        console.log('Confirma TODO')
        this.setState({confirmacao : <div>
                        Deseja mesmo deletar  {objeto.name} | {this.state.card.set}  ?
                        <Button value = "NÃO" clickFunc={() => {
                            this.setState({confirmacao : <></>})}}/>
                        <Button value = "SIM" clickFunc={() => this.deleteEntry()}/>
                      </div>})
    }
    deleteEntry = () =>{
        //const navigate = useNavigate();
        let dataDelete = (this.props.value === "colaborador" ? objeto.matricula : objeto.id)
        Axios.delete(this.state.targetUrl, {data: dataDelete})
        this.setState({redirect : <Navigate to='/' replace/>})
    }


    render(){
        let form = <></>

        switch (this.props.value){
            case "venda":
                form = (<>
                <label>
                    Data da Venda:
                    <input type='date' name='data'   placeholder={objeto.data} onChange={(event) => this.handleFieldChange(event, 1)}/>
                </label><br/>
                <label>
                    Valor total:
                    <input type='number' name='valor' step='0.01'  placeholder={objeto.valor} onChange={(event) => this.handleFieldChange(event, 2)}/>
                </label><br/>
                <label>
                    Matrícula:
                    <input type='number' name='matricula' placeholder={objeto.matricula} onChange={(event) => this.handleFieldChange(event, 3)}/>
                </label>
                </>
                )
                break;
            case "produto":
                form = (<>
                    <label>
                        Nome:
                        <input type='text' name='nome' placeholder={objeto.nome} onChange={(event) => this.handleFieldChange(event, 1)}/>
                    </label><br/>
                    <label>
                        Preço:
                        <input type='number' name='preco' placeholder={objeto.preco} onChange={(event) => this.handleFieldChange(event, 2)}/>
                    </label>
                    </>
                )
                break;
            default:
                console.log("Como?")
          }
        return(
          <div>
            Form de alteração de {this.props.value}
            <form onSubmit={this.handleSubmit}>
                    {form}
                    {/*<label>
                        Nome:
                        <input type='text' name='Nome' onChange={this.handleNameChange} />
                    </label>
                    <label>
                        <input type='number' name='Idade' onChange={this.handleAgeChange}/>
                    </label>
        */}
                    
                <Button type='submit' value = {'Editar '+ objeto.nome + ' | ' + objeto.id + ' !!!'}/>
            </form>
            <br/>
            <Button  clickFunc={() => {this.confirmaDelete()}} value = {'Deletar '+ objeto.nome + ' | ' + objeto.id + ' !!!'}/>
            {this.state.confirmacao}
            {this.state.redirect}
          </div>
        )
    }
}