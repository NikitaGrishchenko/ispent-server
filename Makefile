.PHONY: run
run:
	uvicorn src.main:app --reload

.PHONY: run-backend
run-backend:
	@make run-django-server

.PHONY: clear
clear:
	poetry run task clear

.PHONY: createadmin
createadmin:
	poetry run task createsuperuser

.PHONY: migrate
migrate:
	poetry run task migrate

# Primary commands
.PHONY: install
install:
	@make -j 2 install-backend install-frontend
	poetry run task initconfig --debug
	@make migrate
	poetry run task defaultadmin
	poetry run task defaultfixtures

.PHONY: install-prod
install-prod:
	poetry run pip install -U pip
	@make install-backend-prod
	poetry run task initconfig

.PHONY: build
build:
	poetry run task collectstatic
	@make migrate
	poetry run task defaultadmin
	poetry run task defaultfixtures
