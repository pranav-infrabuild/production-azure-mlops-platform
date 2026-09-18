.PHONY: help test lint format validate

help:
	@echo "Available commands:"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linting"
	@echo "  make format     - Format Python code"
	@echo "  make validate   - Run validation checks"

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

validate:
	terraform fmt -check -recursive infrastructure/terraform
	ruff check .
	pytest