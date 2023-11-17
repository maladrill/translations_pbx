#!/bin/bash

venv_dir="/home/translations"
requirements_url="https://raw.githubusercontent.com/maladrill/translations_pbx/main/requirements.txt"
script_url="https://raw.githubusercontent.com/maladrill/translations_pbx/main/process_translations.py"

# Check if the venv directory exists
if [ ! -d "$venv_dir" ]; then
    # Create virtual environment
    python3 -m venv "$venv_dir"

    # Activate virtual environment
    source "$venv_dir/bin/activate"

    # Download requirements.txt from GitHub
    curl -o "$requirements_file" "$requirements_url"
    
    # Install required packages from requirements.txt
    pip install -r "$requirements_file"
else
    # Activate existing virtual environment
    source "$venv_dir/bin/activate"
fi

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
