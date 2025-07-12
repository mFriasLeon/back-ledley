.PHONY: up shell logs down

# Levanta los servicios con docker-compose (con volumen incluido)
run: up migrate

up:
	docker compose up -d --build

clean:
	docker compose down -v --remove-orphans
	
# Abre una shell interactiva dentro del contenedor 'web'
shell:
	docker exec -it -u $(shell id -u):$(shell id -g) $(shell docker compose ps -q web) /bin/bash

migrate:
	docker exec -it $(shell docker compose ps -q web) poetry run python manage.py migrate

# Muestra logs del contenedor 'web' en tiempo real
logs:
	docker compose logs -f web

# Para y elimina los contenedores
down:
	docker compose down

format:
	@echo "Fixing code with ruff"
	poetry run ruff format .
	@echo "Running ruff check linting..."
	poetry run ruff check .
