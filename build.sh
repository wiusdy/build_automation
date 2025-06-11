#!/bin/bash
set -e  # Para o script em caso de erro

echo "🔍 Rodando black..."
black --check .

echo "🧪 Rodando testes..."
pytest

echo "🚨 Rodando pre-commit..."
pre-commit run --all-files
