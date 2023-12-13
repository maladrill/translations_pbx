#!/bin/bash

repo_url="https://raw.githubusercontent.com/maladrill/translations_pbx/main"
venv_dir="/home/translations"
requirements_file="$venv_dir/requirements.txt"
script_file="$venv_dir/process_translations.py"
uninstall_file="$venv_dir/uninstall.py"

# Check if /home/translations directory exists, and create it if not
if [ ! -d "$venv_dir" ]; then
    mkdir -p "$venv_dir"
fi

# Check if Python 3.6 or higher is available
if command -v python3.6 &>/dev/null; then
    python_cmd="python3.6"
elif command -v python3 &>/dev/null; then
    python_cmd="python3"
else
    echo "Error: Python 3.6 or higher is required, but not found."
    exit 1
fi

# Create and activate the virtual environment if it doesn't exist
if [ ! -d "$venv_dir/env" ]; then
    $python_cmd -m venv "$venv_dir/env"
    source "$venv_dir/env/bin/activate"
    pip install -r "$requirements_file"
else
    source "$venv_dir/env/bin/activate"
fi

# Download requirements.txt, process_translations.py, and uninstall.py from GitHub
curl -o "$requirements_file" "$repo_url/requirements.txt"
curl -o "$script_file" "$repo_url/process_translations.py"
curl -o "$uninstall_file" "$repo_url/uninstall.py"

# Check if the Python script file exists
if [ -f "$script_file" ]; then
    # Run the script
    python "$script_file"
else
    echo "Error: $script_file not found in $venv_dir"
    exit 1
fi

# Deactivate the virtual environment
deactivate
# Display Info
echo "Jeśli chcesz usunąć tłumaczenie wydaj komendę: /home/translations/env/bin/python /home/translations/uninstall.py"
