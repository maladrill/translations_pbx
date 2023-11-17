#!/bin/bash

venv_dir="/home/translations"

# Check if the venv directory exists
if [ ! -d "$venv_dir" ]; then
    # Create virtual environment
    python3 -m venv "$venv_dir"

    # Activate virtual environment
    source "$venv_dir/bin/activate"

    # Download the requirements.txt file from GitHub
    curl -o "$venv_dir/requirements.txt" https://raw.githubusercontent.com/maladrill/translations_pbx/main/requirements.txt

    # Install required packages from requirements.txt
    pip install -r "$venv_dir/requirements.txt"
else
    # Activate existing virtual environment
    source "$venv_dir/bin/activate"
fi

# Download the Python script
curl -o "$venv_dir/process_translations.py" https://raw.githubusercontent.com/maladrill/translations_pbx/main/process_translations.py

# Run the script
python "$venv_dir/process_translations.py"

# Deactivate the virtual environment
deactivate
