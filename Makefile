.PHONY: up
up:
	-docker-compose --file docker-compose.dev.yml up
.PHONY: down
down:
	-docker-compose --file docker-compose.dev.yml down