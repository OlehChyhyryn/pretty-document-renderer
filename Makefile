SOURCE_DIR := src

pre-commit: lint build
	tox run -e py38,py39,py310,py311,py312,mypy,flake8,black,isort

build:
	poetry build

setup:
	poetry install --no-root --with dev

update:
	poetry update

black:
	poetry run black $(SOURCE_DIR)

isort:
	poetry run isort $(SOURCE_DIR)

mypy:
	poetry run mypy $(SOURCE_DIR)

flake8:
	poetry run flake8 $(SOURCE_DIR) --count --statistics

lint: black isort flake8 mypy