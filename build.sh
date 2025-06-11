#!/bin/bash
set -e

echo "🔧 Formatando código com black..."
black .

echo "🧪 Rodando testes..."
pytest

echo "🚨 Rodando pre-commit..."
pre-commit run --all-files
