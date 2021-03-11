#!/bin/bash
set -euxo pipefail

poetry run isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=79 neuroio/ tests/
poetry run black neuroio/ tests/ -l 79
