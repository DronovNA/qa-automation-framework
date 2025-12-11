.PHONY: help install setup test test-mobile test-pwa test-coverage lint format type-check clean

help:
	@echo "QA Automation Framework - Available Commands"
	@echo "============================================="
	@echo ""
	@echo "Setup:"
	@echo "  make install        - Install all dependencies"
	@echo "  make setup          - Run setup script"
	@echo ""
	@echo "Testing:"
	@echo "  make test           - Run all tests"
	@echo "  make test-mobile    - Run mobile tests only"
	@echo "  make test-pwa       - Run PWA tests only"
	@echo "  make test-coverage  - Run tests with coverage"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint           - Run linting (flake8)"
	@echo "  make format         - Format code (black, isort)"
	@echo "  make type-check     - Run type checking (mypy)"
	@echo "  make quality        - Run all quality checks"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean          - Clean up generated files"
	@echo "  make pre-commit     - Install pre-commit hooks"

install:
	pip install --upgrade pip setuptools wheel
	cd mobile && pip install -r requirements.txt && cd ..
	cd pwa && pip install -r requirements.txt && cd ..
	playwright install

setup:
	@bash scripts/setup.sh

test:
	pytest mobile/tests/ pwa/tests/ -v --tb=short

test-mobile:
	cd mobile && pytest tests/ -v --tb=short

test-pwa:
	cd pwa && pytest tests/ -v --tb=short

test-coverage:
	pytest mobile/tests/ pwa/tests/ --cov=mobile.src --cov=pwa.src --cov-report=html --cov-report=term

lint:
	flake8 mobile/src mobile/tests pwa/src pwa/tests

format:
	black mobile pwa --line-length=100
	isort mobile pwa --profile black

type-check:
	mypy mobile/src pwa/src --ignore-missing-imports

quality: lint type-check
	@echo "All quality checks passed!"

clean:
	rm -rf __pycache__ .pytest_cache .mypy_cache .coverage
	rm -rf mobile/__pycache__ mobile/.pytest_cache
	rm -rf pwa/__pycache__ pwa/.pytest_cache
	rm -rf reports/
	find . -type d -name '*.egg-info' -exec rm -rf {} +

pre-commit:
	pip install pre-commit
	pre-commit install
