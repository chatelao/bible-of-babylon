#!/bin/bash
# Install development dependencies for the comparative book project.

set -e

echo "Installing Jinja2..."
pip install jinja2

echo "Installing ANTLR4 tools..."
pip install antlr4-tools

echo "Development environment setup complete."
