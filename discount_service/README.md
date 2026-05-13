# FOSSDEV Docker Practice

## Описание

Проект представляет собой систему обработки заказов из нескольких FastAPI-сервисов.

Сервисы:

- `product-service` — хранит информацию о товарах;
- `discount-service` — рассчитывает скидки;
- `order-service` — создаёт заказы;
- `db` — PostgreSQL для хранения заказов.

## Docker Compose

```bash
docker compose up --build
docker compose down
```

## Makefile

```bash
make test
make build
make compose-up
make compose-down
make smoke
make check
```
