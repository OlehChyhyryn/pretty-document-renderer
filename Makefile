SOURCE_DIR := src

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