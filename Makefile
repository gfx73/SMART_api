.PHONY: docker-build
docker-build:
	docker build -t smart_api .

.PHONY: up
up:
	docker run --env-file .env -p 8084:8084 --dns 8.8.8.8 smart_api
