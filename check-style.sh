#!/usr/bin/env bash

# Run code style checks on the semitone project.
# Fails fast with non-zero status if any check fails.

set -e

CHECK_DIRS=$(find . -maxdepth 2 -type f -name "*.py" | sed 's|/[^/]*\.py$||' | sort -u | tr '\n' ' ')
echo "Analyzing directories: $CHECK_DIRS"
echo ""

echo "Running Black..."
black --line-length 80 $CHECK_DIRS

echo ""
echo "Running Pylint..."
pylint $CHECK_DIRS

echo ""
echo "Running Mypy..."
mypy --ignore-missing-imports $CHECK_DIRS

echo ""
echo "✓ All checks passed!"