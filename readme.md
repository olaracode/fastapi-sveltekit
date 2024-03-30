# Fastapi[psql + redis] & ⚡ Svelte[Skeleton-UI] Docker container 🐳

Fullstack app container using Fastapi, Svelte, Postgres, Redis, and Docker.

## Requirements

- Docker
- Docker-compose

## Installation

### 1. First clone the repository

```bash
git clone https://github.com/olaracode/fast-svelte-docker
```

### 2. Then set up your environment variables, for easier maintainability we use a single .env file for all services.

```bash
cp .env.example .env
```

### 3. Fill .env

- 1. Set the `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` to your desired values.

- 2. Generate a KEY and REFRESH_KEY

  Both the `KEY` and `REFRESH_KEY` are used to sign the JWT tokens, you can generate them using the following command.

  We use the simple `openssl` command to generate the keys.

  ```bash
  openssl rand -hex 32
  ```

### 4. Build the containers

```bash
docker-compose up --build
```

### 5. With the containers running you need to run:

- DB Migrations

  ```bash
  docker-compose exec web alembic revision --autogenerate
  ```

- DB Upgrade

  ```bash
  docker-compose exec web alembic upgrade head
  ```

# Misc docker commans

## Start & build containers

```bash
docker-compose up --build
```

## access to the docker terminal

```bash
docker-compose exec <service_name> bash
```

## Down all containers and remove volumes

```bash
docker-compose down -v
```

## To recreate services(when you change the docker-compose file and want to apply the changes)

```bash
docker-compose up --build
```

## To recreate services and remove volumes

```bash
docker-compose up --build -V
```

## To recreate services and remove volumes and build the images

```bash
docker-compose up --force-recreate
```
