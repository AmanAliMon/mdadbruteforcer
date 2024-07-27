#!/bin/bash

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip not found, installing pip..."
    python -m ensurepip
fi
cd engine
# Create and activate a virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install selenium rich

# Run k.py
python k.py
