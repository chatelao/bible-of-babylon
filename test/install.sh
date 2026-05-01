#!/bin/bash
# Install testing-specific dependencies for the comparative book project.

set -e

echo "Installing pytest..."
pip install pytest

echo "Installing Sphinx for documentation testing..."
pip install sphinx

echo "Testing environment setup complete."
