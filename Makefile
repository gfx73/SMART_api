.PHONY: docker-build
docker-build:
	docker build -t gfx73/smart_api .

.PHONY: up
up:
	docker compose up -d

.PHONY: pull
pull:
	docker image pull gfx73/smart_api

.PHONY: push
push:
	docker push gfx73/smart_api

.PHONY: stop
stop:
	docker compose down

.PHONY: logs
logs:
	docker compose logs -f smart-api
