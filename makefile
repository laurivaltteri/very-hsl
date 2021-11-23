.PHONY: build
build:
	cd ./dev; docker-compose -f docker-compose.yml build 2>&1 | tee buildlog.txt

.PHONY: start
start: build
	cd ./dev; docker-compose -f docker-compose.yml up -d

.PHONY: stop
stop:
	cd ./dev; docker-compose -f docker-compose.yml down

.PHONY: logs
logs:
	cd ./dev; docker-compose -f docker-compose.yml logs -f