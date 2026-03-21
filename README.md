# CineReserve
API backend para gerenciamento de cinema — permite cadastrar filmes, sessões, reservar assentos e gerar tickets digitais.

Projeto desenvolvido para o processo seletivo de estágio da B2BIT

# Tecnologias
- Python 3 / Django REST Framework
- Poetry
- PostgreSQL
- JWT (SimpleJWT)
- Postman

## Como rodar o projeto

### Pré-requisitos
- Python 3.12+
- Poetry
- PostgreSQL

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/cinereserve.git
cd cinereserve
```

2. Instale as dependências:
```bash
poetry install
```

3. Crie o arquivo `.env` baseado no `.env.example`:
```bash
cp .env.example .env
```

4. Crie o banco de dados no PostgreSQL:
```bash
sudo -u postgres psql
CREATE DATABASE cinereserve;
\q
```

5. Rode as migrations:
```bash
poetry run python manage.py migrate
```

6. Suba o servidor:
```bash
poetry run python manage.py runserver
```
---------------------------
## Endpoints

### Autenticação
- POST `/auth/register/` — cadastro de usuário
- POST `/auth/login/` — login e geração de token JWT
- POST `/auth/refresh/` — renovar token

### Filmes
- GET `/movies/` — listar filmes
- GET `/movies/?session[id]` — listar filmes de uma sessão específica
- POST `/movies/` — cadastrar filme

### Sessões
- GET `/sessions/` — listar sessões
- GET `/sessions/?movie=1` — listar sessões de um filme
- POST `/sessions/` — cadastrar sessão

### Assentos
- GET `/seats/?session=1` — mapa de assentos de uma sessão
- POST `/seats/` — cadastrar assento

### Reservas
- POST `/reservations/` — reservar um assento
- POST `/reservations/1/checkout/` — finalizar reserva e gerar ticket

### Tickets
- GET `/tickets/` — meus tickets

----------------------------
## Variáveis de ambiente

Crie um arquivo `.env` baseado no `.env.example`:
```env
SECRET_KEY=sua-chave-secreta
DEBUG=True
DB_NAME=cinereserve
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```