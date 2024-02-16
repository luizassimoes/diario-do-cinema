# Diário do Cinema

**Projeto de Gerenciamento de Filmes**

Este é um projeto de software desenvolvido em Python, utilizando o framework Flask, para gerenciar uma lista pessoal de filmes. A aplicação permite ao usuário adicionar filmes que deseja assistir, registrar os filmes que já assistiu, atribuir notas e registrar as datas de visualização.

### Funcionalidades Principais

- CRUD de Filmes
- Registro de Notas e Datas de Visualização
- Organização

### Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada no desenvolvimento do projeto.
- **Flask**: Framework web utilizado para criar a aplicação.
- **Flask WTForms**: Extensão do Flask para lidar com formulários web.
- **SQLAlchemy**: Ferramenta de mapeamento objeto-relacional (ORM) utilizada para interagir com o banco de dados.
- **HTML, CSS e Bootstrap**: Tecnologias web utilizadas para criar a interface do usuário da aplicação.
- **MySQL**: Banco de dados utilizado para armazenar os dados dos filmes.

## Como Executar o Projeto

1. Clone este repositório em sua máquina local.
2. Instale as dependências do projeto usando o comando `pip install -r requirements.txt`.
3. Execute o arquivo `app.py` para iniciar o servidor Flask.
4. Acesse a aplicação em seu navegador utilizando o endereço [http://localhost:5000](http://localhost:5000).

- Atenção! Como o banco de dados está conectado ao localhost, crie um arquivo config.txt com o formato a seguir para ver sua própria lista de filmes.

| Chave       | Valor       |
|-------------|-------------|
| SECRET_KEY  | sua_chave   |
| senha       | sua_senha   |
| SGBD        | seu_sgbd    |
| usuario     | seu_user    |
| servidor    | localhost   |
| database    | sua_database|

Para mais detalhes, consulte o repositório no GitHub ou entre em contato através do e-mail [luizassimoes@hotmail.com](mailto:luizassimoes@hotmail.com).
