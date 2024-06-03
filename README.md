# API de Geração e Gerenciamento de Histórias Interativas

Esta API permite a criação, gerenciamento e geração de histórias interativas, oferecendo uma plataforma para aplicações em conteúdo dinâmico, escrita colaborativa, jogos narrativos e educação.

## Funcionalidades

- **CRUD de Histórias**: Criação, leitura, atualização e remoção de histórias.
- **Gestão de Usuários**: Registro e gerenciamento de usuários.
- **Geração de Conteúdo**: Integração com a API do ChatGPT para geração dinâmica de partes de histórias.

## Tecnologias Utilizadas

- FastAPI
- SQLAlchemy para gerenciamento de banco de dados
- Pydantic para validação de dados
- PostgreSQL ou SQLite
- pytest para testes unitários e de integração

## Configuração do Ambiente

### Pré-requisitos

É necessário ter Python 3.6+ instalado. Recomenda-se o uso de um ambiente virtual (venv) para a instalação das dependências.

### Instalação de Dependências

Execute o seguinte comando para instalar as dependências necessárias:

```bash
pip install -r requirements.txt

```
## Configuração do Banco de Dados

Por padrão, o projeto usa SQLite para desenvolvimento e testes.

Execução da Aplicação
Para iniciar o servidor, execute:

```bash

uvicorn app.main:app --reload
```

A opção --reload faz com que o servidor reinicie automaticamente após mudanças no código.

### Documentação da API

Após iniciar a aplicação, a documentação interativa Swagger UI está disponível em:

```bash

http://localhost:8000/docs
```

Para ReDoc, acesse:

```bash

http://localhost:8000/redoc
```

### Testes
Para executar os testes unitários e de integração, navegue até a pasta raiz do projeto e execute:

```bash

pytest
```

### Estrutura do Projeto

/ponderada-7
|-- app/
|   |-- __init__.py
|   |-- crud.py
|   |-- database.py
|   |-- main.py
|   |-- models.py
|   |-- schemas.py
|-- tests/
|   |-- __init__.py
|   |-- test_config.py
|   |-- test_stories_crud.py
|   |-- test_users_crud.py
|   |-- conftests.py
|-- README.md