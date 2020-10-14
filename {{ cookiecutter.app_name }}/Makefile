build:
	docker build .

idea-configuration:
	python .dev/idea/prepare_idea.py

format:
	python -m black .

test:
	python -m pytest

static-typing:
	python -m mypy {{ cookiecutter.app_name }}