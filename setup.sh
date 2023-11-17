#!/bin/bash

venv_dir="/home/translations"
requirements_file="$venv_dir/requirements.txt"
script_file="$venv_dir/process_translations.py"
requirements_url="https://raw.githubusercontent.com/maladrill/translations_pbx/main/requirements.txt"
script_url="https://raw.githubusercontent.com/maladrill/translations_pbx/main/process_translations.py"

# Check if Python3 is installed
if ! command -v python3.6 &>/dev/null; then
    echo "Error: Python3 is not installed."
    exit 1
fi

# Check if venv directory exists
if [ ! -d "$venv_dir" ]; then
    # Create virtual environment
    python3.6 -m venv "$venv_dir"
fi

# Activate virtual environment
source "$venv_dir/bin/activate"

# Download requirements.txt from GitHub
curl -o "$requirements_file" "$requirements_url"

# Install required packages from requirements.txt
pip install -r "$requirements_file"

# Download process_translations.py from GitHub
curl -o "$script_file" "$script_url"

# Check if the Python script file exists
if [ -f "$script_file" ]; then
    # Run the script
    python "$script_file"
else
    echo "Error: process_translations.py not found in $venv_dir"
    exit 1
fi

# Deactivate the virtual environment
deactivate
