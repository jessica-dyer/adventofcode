setup:
	poetry install

lint: setup
	poetry run black .
	poetry run ruff . --fix