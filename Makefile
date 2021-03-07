BROWSER := xdg-open

ifeq ($(OS),Windows_NT)
    BROWSER := start
endif

.PHONY: docs

setup:
	@python -m pip install --upgrade pip
	@pip3 install pip-tools
	@pip-sync requirements/dev.txt && pip3 install -e .
	@pre-commit install -c ./.githooks/.pre-commit-config.yaml

freeze:
	@pip-compile requirements/test.in
	@pip-compile requirements/docs.in
	@pip-compile requirements/dev.in

build: clean-build
	@python -m build --wheel
	@docker-compose build

clean-build:
	@rm -rf ./build
	@rm -rf ./dist

dev: build
	@docker-compose up

test:
	@python -m unittest discover -v

lint:
	@pylint ./src/serenity


coverage: clean-coverage
	@coverage run -m unittest discover -v
	@coverage html
	@$(BROWSER) "./htmlcov/index.html"

clean-coverage:
	@rm -rf ./htmlcov
	@rm -rf .coverage

docs: clean-docs
	@sphinx-build -b html docs build/docs
	@$(BROWSER) "./build/docs/index.html"

clean-docs:
	@rm -rf ./build/docs

tox: clean-tox
	@tox -c ./setup.cfg

clean-tox:
	@rm -rf .tox

clean: clean-coverage clean-docs clean-build clean-tox

clean-all: clean
	@rm -rf ./src/*.egg-info
	@rm -rf ./venv