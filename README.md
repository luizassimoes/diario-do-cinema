<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <div class="container">
      <h1>Diário do Cinema</h1>
        <p><b>Projeto de Gerenciamento de Filmes</b></p>
        <p>Este é um projeto de software desenvolvido em Python, utilizando o framework Flask, para gerenciar uma lista pessoal de filmes. A aplicação permite ao usuário adicionar filmes que deseja assistir, registrar os filmes que já assistiu, atribuir notas e registrar as datas de visualização.</p>
        <h3>Funcionalidades Principais</h3>
        <ul>
            <li>CRUD de Filmes</li>
            <li>Registro de Notas e Datas de Visualização</li>
            <li>Organização</li>
        </ul>
        <h3>Tecnologias Utilizadas</h3>
        <ul>
            <li><b>Python</b>: Linguagem de programação principal utilizada no desenvolvimento do projeto.</li>
            <li><b>Flask</b>: Framework web utilizado para criar a aplicação.</li>
            <li><b>Flask WTForms</b>: Extensão do Flask para lidar com formulários web.</li>
            <li><b>SQLAlchemy</b>: Ferramenta de mapeamento objeto-relacional (ORM) utilizada para interagir com o banco de dados.</li>
            <li><b>HTML, CSS e Bootstrap</b>: Tecnologias web utilizadas para criar a interface do usuário da aplicação.</li>
            <li><b>MySQL</b>: Banco de dados utilizado para armazenar os dados dos filmes.</li>
        </ul>
        <h2>Como Executar o Projeto</h2>
        <ol>
            <li>Clone este repositório em sua máquina local.</li>
            <li>Instale as dependências do projeto usando o comando <code>pip install -r requirements.txt</code>.</li>
            <li>Execute o arquivo <code>app.py</code> para iniciar o servidor Flask.</li>
            <li>Acesse a aplicação em seu navegador utilizando o endereço <a href="http://localhost:5000">http://localhost:5000</a>.</li>
        </ol>
        <ul>
            <li>Atenção! Como o banco de dados está conectado ao localhost, crie um arquivo config.txt com o formato a seguir para ver sua própria lista de filmes.</li>
        </ul>
        <ul>    
        <table>
            <tr>
                <td>SECRET_KEY</td>
                <td>sua_chave</td>
            </tr>
            <tr>
                <td>senha</td>
                <td>sua_senha</td>
            </tr>
            <tr>
                <td>SGBD</td>
                <td>seu_sgbd</td>
            </tr>
            <tr>
                <td>usuario</td>
                <td>seu_user</td>
            </tr>
            <tr>
                <td>servidor</td>
                <td>localhost</td>
            </tr>
            <tr>
                <td>database</td>
                <td>sua_database</td>
            </tr>
        </ul>
    </table>
            
        <p>Para mais detalhes, consulte o <a href="https://github.com/luizassimoes/lu-e-thi">repositório no GitHub</a> ou entre em <a href="mailto:luizassimoes@hotmail.com">contato</a>.</p>
    </div>
</body>
</html>
