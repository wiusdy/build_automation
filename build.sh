#!/bin/bash
set -e

echo "🔍 Rodando black..."
black --check .

echo "🔍 Rodando isort..."
isort --check-only --skip venv .

echo "🔍 Rodando flake8..."
flake8 --exclude=venv .

echo "🚨 Rodando pre-commit hooks..."
pre-commit run --all-files

echo "🧪 Rodando testes..."
pytest
