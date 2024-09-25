.PHONY: docker-build
docker-build:
	docker build -t gfx73/smart_api .

.PHONY: up
up:
	docker rm -f smart_api || true
	docker run -p 8084:8084 --env-file .env --dns 8.8.8.8 --restart always -d --name smart_api gfx73/smart_api

.PHONY: pull
pull:
	docker image pull gfx73/smart_api
