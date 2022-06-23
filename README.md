<h1 align="center">Projeto de C214-L6 - API para venda de produtos em Django - Python</h1>

[![Exercicio01](https://github.com/G-ilian/Projeto_C214-Lab/actions/workflows/CIProjeto.yml/badge.svg)](https://github.com/G-ilian/Projeto_C214-Lab/actions)

<p align="center">
    <img src="https://prosperaerp.com/blog/wp-content/uploads/2018/04/registrar-compras.jpg">
</p>
Imagem retirada do site Prospera.erp: https://prosperaerp.com/blog/  

### :books: Descrição

<p>Projeto de C214-L6, laboratório da disciplina de Engenharia de Software.</p>
<p>Essa API para venda de produtos possui como finalidade cadastrar clientes, produtos e compras em um banco de dados relacional, onde vários clientes possam comprar vários produtos.</p>
<p> - Cada cliente deve ter um CPF para identificação única, um nome, o seu CEP, um e-mail, uma senha única (aceita letras, números e caracteres especiais) e a informação opcional de telefone. </p>
<p> - Cada produto deve ter uma identificação única, um nome, uma marca, um tipo (smartphones, periféricos, eletrônicos em geral, etc.), o seu preço (aceita centavos) e a quantidade disponível no estoque. </p>
<p> - Um cliente pode comprar vários produtos assim como um produto é comprado por muitos clientes. Toda Compra possui um valor total (aceita centavos), um tipo de pagamento (cartão ou boleto, por exemplo), um código de rastreamento único e a quantidade comprada. </p>

#### Projeto
- Na construção dessa API foi utilizado a linguagem Python com o framework Django, específico para aplicações web. Já o banco de dados, utilizamos o SQLite por ser o banco padrão do framework Django e por ser simples de trabalhar. A preferência pelo Python foi por questões de familiaridades que ambos os desenvolvedores possuem, já o framework Django por ser robusto e mais abrangente.
- Algumas dependências de projeto que valem ser mercionada são:</p>
<p> - Django Rest Framework: Uma Biblioteca complementar que não vem no framework Django por padrão, é responsável por criar a API seguindo o padrão REST.</p>

### :computer: Funcionalidades dos Projetos
#### Funcionalidades
- Cadastra novos clientes e produtos;
- Cadastra compras, inserindo as informações na tabela compra;
- Cancela uma compra, removendo as informações na tabela compra;
- Atualiza dados de clientes e produtos
- Exclui clientes e produtos cadastrados;
- Busca por compras realizadas por determinado cliente mostrando o nome do cliente e do produto, o valor de compra pago e o tipo de pagamento.

### :hammer_and_wrench: Instalação e Execução
#### Preparação do ambiente no computador para executar a API
- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows)
- [Postman](https://www.postman.com/downloads/)

Observação: Você pode usar a IDE e o criente HTTP de sua preferência, o Visual Studio Code, PyCharm, o Postman são apenas sugestões. O próprio framework Django já traz uma documentação semelhante ao Swagger onde é possível testar os métodos http.

Clone o repositório em seu computador para poder acessar o projeto:
```
git clone git@github.com:G-ilian/Projeto_C214-Lab.git
```
Para acessar o repositório clonado usando o terminal, digite: 
```
cd Projeto_C214-Lab
```
Para acessar os arquivos de código pelo terminal, digite:
```
cd vendas
```

#### Instalando as dependências
* Criando ambiente virtual para instalar as dependências do Python de maneira isolada:
```
python -m venv venv
```
* Iniciando ambiente virtual no Windows:
```
venv\Scripts\activate
```
* Iniciando ambiente virtual no Linux ou MAC:
```
source venv\bin\activate
```
* Instalando as dependências no ambiente virtual:
```
pip install -r requirements.txt
```
* Realizando a migração para a contrução do Banco de Dados da API:
```
python manage.py migrate
```
* Iniciando cliente Python
```
python manage.py runserver
```
#### Acessando API pela internet
* Pelo deploy realizado no Heroku, é possível acessar a API de qualquer lugar, usando o link: https://vendas-c214.herokuapp.com/

#### Realizando os testes 

<p>Quando pensamos em um software maduro, uma das características mais importantes e destacavéis são os testes podendo ser estes de unidade, integração, mock e afins, em nosso projeto temos também diversos destes testes, que podem ser realizados de forma local através do seguinte comando : </p>

* Testando as funcionalidades do projeto
```
python manage.py test
```
Apresentação do projeto: https://youtu.be/TvK1jGL_i2g 

## :gear: Autor

* **Flávio Henrique Madureira Bergamini** - [Flávio](https://github.com/flaviobergamini)

* **Gabriel Ilian Fonseca Barboza** - [Gabriel](https://github.com/G-ilian) 

Sob a orientação da monitora:
* **Rafaela de Moraes Papale** - [Rafaela](https://github.com/RafaelaPapale)
