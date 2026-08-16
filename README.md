# CRUD de Temporadas

Projeto desenvolvido em Flask para realizar o cadastro e gerenciamento de temporadas e episódios de uma áudio série.

## Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- Jinja2
- ORM

## Funcionalidades

O sistema permite:

- Cadastrar temporadas;
- Visualizar temporadas;
- Editar temporadas;
- Excluir temporadas;
- Cadastrar episódios;
- Visualizar episódios;
- Editar episódios;
- Excluir episódios;
- Relacionar episódios às suas respectivas temporadas;
- Armazenar os dados em banco de dados SQLite;
- Utilizar ORM através do Flask-SQLAlchemy.

## Estrutura do projeto

```text
cadastro_temporadas/
├── docs/
├── └── historico-chatgpt.md
├── instance/
│   └── temporadas.db
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── base.html
│   ├── cadastrar_episodio.html
│   ├── cadastrar_temporada.html
│   ├── editar_episodio.html
│   ├── editar_temporada.html
│   ├── episodios.html
│   ├── index.html
│   └── temporadas.html
├── .gitignore
├── app.py
└── README.md
```

## Como executar

### 1. Clonar o projeto

```bash
git clone https://github.com/Flask-Web-Development/2026-crud-marcos.git
```

### 2. Entrar na pasta do projeto

```bash
cd 2026-crud-marcos
```

### 3. Instalar as dependências

```bash
pip install flask flask-sqlalchemy
```

### 4. Executar o projeto

```bash
flask --app app run --debug
```

### 5. Acessar no navegador

```text
http://127.0.0.1:5000
```

## Banco de dados

O projeto utiliza SQLite como banco de dados.

O Flask-SQLAlchemy é utilizado para facilitar a comunicação entre a aplicação Flask e o banco de dados através de ORM (Object-Relational Mapping).

Os dados são armazenados no arquivo:

```text
instance/temporadas.db
```

## Modelos

O sistema possui dois modelos principais:

### Temporada

Uma temporada possui:

- ID;
- Título;
- Descrição;
- Data de publicação;
- Status.

### Episódio

Um episódio possui:

- ID;
- Número;
- Título;
- Descrição;
- Data de publicação;
- Temporada relacionada.

Os episódios possuem um relacionamento com as temporadas através da chave estrangeira `temporada_id`.

## CRUD

O projeto implementa as quatro operações principais do CRUD:

- **Create:** cadastro de temporadas e episódios;
- **Read:** visualização de temporadas e episódios;
- **Update:** edição de temporadas e episódios;
- **Delete:** exclusão de temporadas e episódios.
````
