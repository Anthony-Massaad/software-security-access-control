#!/bin/bash
if command -v python3 &> /dev/null; then
    echo "Using Python 3"
    python3 -m unittest src/tests/test_*.py
elif command -v python &> /dev/null; then
    echo "Using Python 2"
    python -m unittest src/tests/test_*.py
else
    echo "Error: Python not found. Please install Python version 3.8 or > to run the tests."
    exit 1
fi