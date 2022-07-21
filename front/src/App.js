import './App.css';
import {Routes, Route} from "react-router-dom";
import Page from './routes/Page.js';
import FormPage from './routes/FormPage.js';
import InfoPage from './routes/InfoPage.js';
import Header from './components/header';
import Button from './components/button';
import UpdateForm from './components/updateForm.js'

export default function App() {
  return (
    <div>
      <Header clickFunc={()=> {
            console.log(window.location.pathname)
            console.log("Isso vai pra página inicial")
            
          }}
            />


      <Routes>
        <Route path='/*' element = {
          <div>
            Página Inicial
            <Button value="Colaboradores" 
            clickFunc={() => {
            console.log("Isso vai pra página de Colaboradores")
            }}
            link='/colaborador'
            />
            <Button value="Vendas" 
            clickFunc={() => {
            console.log("Isso vai pra página de Colaboradores")
            }}
            link='/venda'
            />
            <Button value="Produtos" 
            clickFunc={() => {
            console.log("Isso vai pra página de Colaboradores")
            }}
            link='/produto'
            />
          </div>

        }/>  
        <Route path='/colaborador' element={
          <Page type="colaborador"/>
        }/>
        <Route path='/venda' element={
          <div>
            <Page type="venda"/> 
            <Button value='Novo' link='./novaVenda'/>
          </div>
        }/>
        <Route path='/produto' element={
          <div>
            <Page type="produto"/> 
            <Button value="Novo" link='./novoProduto'/>
          </div>
        }/>
        <Route path='/venda/NovaVenda' element={
          <FormPage value='venda'/>
        }/>
        <Route path='/produto/novoProduto' element={
          <FormPage value='produto'/>
        }/>
        <Route path='/colaborador/id/*' element={
          <div>
          <InfoPage value='colaborador'/>
          </div>
        }/>
        <Route path='/venda/id/*' element={
          <div>
            <InfoPage value='venda'/>
            <UpdateForm value = 'venda'/>
          </div>
        }/>
        <Route path='/produto/id/*' element={
          <div>
          <InfoPage value='produto'/>
          <UpdateForm value = 'produto'/>
          </div>
        }/>
      </Routes>
    </div>
  );
}

