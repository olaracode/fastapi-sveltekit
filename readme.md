# Fastapi + PSQL + Redit Container

## Description

# Commands

```bash
docker-compose up --build
```

## migrate database

```bash
docker-compose exec web alembic revision --autogenerate
```

## upgrade database

```bash
docker-compose exec web alembic upgrade head
```

## access to the docker terminal

```bash
docker-compose exec <service_name> bash
```

## Create a ssl key(KEY | REFRESH_KEY)

```bash
openssl rand -hex 32
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
