.DEFAULT_GOAL := check

.PHONY: create-practice remove-practice install test build compose-up compose-down smoke check

create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Creating practice"
	mkdir -p $(PRACTICE)
	cp PracticeMakefile $(PRACTICE)/Makefile

remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	rm -rf $(PRACTICE)

install:
	cd product_service && poetry install
	cd discount_service && poetry install
	cd order_service && poetry install

test:
	cd discount_service && PYTHONPATH=src poetry run pytest

build:
	docker build -t product-service:local ./product_service
	docker build -t discount-service:local ./discount_service
	docker build -t order-service:local ./order_service

compose-up:
	docker compose up --build

compose-down:
	docker compose down

smoke:
	curl http://127.0.0.1:8002/health
	curl -X POST http://127.0.0.1:8002/orders \
		-H "Content-Type: application/json" \
		-d '{"product_id":"pencil","quantity":2,"promo_code":"STUDENT10"}'

check: test build
	@echo "Project checks completed"