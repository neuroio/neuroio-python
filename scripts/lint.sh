#!/bin/bash
set -euxo pipefail

poetry run mypy --disallow-untyped-defs --ignore-missing-imports neuroio/
poetry run isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=79 --recursive --check --diff --recursive neuroio/ tests/
poetry run black --check -l 79 neuroio/ tests/
poetry run flake8 neuroio/ tests/ --max-line 79 --ignore F403,F401,W503,E203
poetry run safety check
poetry run bandit -r neuroio/
