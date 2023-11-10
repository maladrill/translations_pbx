#!/bin/bash

# Create virtual environment
python3 -m venv /home/translations

# Activate virtual environment
source /home/translations/bin/activate

# Install required packages
pip install certifi==2023.7.22
pip install charset-normalizer==2.0.12
pip install idna==3.4
pip install requests==2.27.1
pip install urllib3==1.26.18

# Download the Python script
curl -o /home/process_translations.py https://raw.githubusercontent.com/maladrill/translations_pbx/main/process_translations.py

# Run the script
python /home/process_translations.py

# Deactivate the virtual environment
deactivate
