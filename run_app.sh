#!/bin/bash
if command -v python3 &> /dev/null; then
    echo "Using Python 3. Running command: 'python3 user_interface.py'"
    python3 user_interface.py
elif command -v python &> /dev/null; then
    echo "Using Python 2. Running command: 'python user_interface.py'"
    python user_interface.py
else
    echo "Error: Python not found. Please install Python version 3.8 or greater to run the app"
    exit 1
fi