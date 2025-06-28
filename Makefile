.PHONY: up shell logs down

# Levanta los servicios con docker-compose (con volumen incluido)
up:
	docker compose up -d --build

# Abre una shell interactiva dentro del contenedor 'web'
shell:
	docker exec -it -u $(shell id -u):$(shell id -g) $(shell docker compose ps -q web) /bin/bash


# Muestra logs del contenedor 'web' en tiempo real
logs:
	docker compose logs -f web

# Para y elimina los contenedores
down:
	docker compose down
