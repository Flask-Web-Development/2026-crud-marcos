# CRUD de Temporadas

Projeto desenvolvido em Flask para realizar o cadastro e gerenciamento de temporadas e episódios.

## Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- Jinja2

## Funcionalidades

O sistema permite:

- Cadastrar temporadas;
- Editar temporadas;
- Cadastrar episódios;
- Editar episódios;
- Visualizar temporadas e episódios;
- Armazenar os dados em banco de dados.

## Estrutura do projeto

```text
cadastro_temporadas/
├── instance/
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── cadastrar_episodio.html
│   ├── cadastrar_temporada.html
│   ├── editar_episodio.html
│   ├── editar_temporada.html
│   └── temporadas.html
├── app.py
└── models.py
```

## Como executar

### 1. Clonar o projeto

```bash
git clone https://github.com/Flask-Web-Development/2026-crud-marcos.git
```

### 2. Entrar na pasta

```bash
cd 2026-CRUD-MARCOS
```

### 3. Instalar as dependências

```bash
pip install flask flask-sqlalchemy
```

### 4. Executar o projeto

```bash
python app.py
```

### 5. Acessar no navegador

```text
http://127.0.0.1:5000
```

## Banco de dados

O projeto utiliza SQLite para armazenar os dados e Flask-SQLAlchemy para facilitar a comunicação entre a aplicação e o banco de dados através de ORM.