import requests
import os
import logging
import shutil
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO)

# List of modules to download translations for
modules = [
    "announcement", "arimanager", "asterisk-cli", "asteriskinfo", "backup", "blacklist", "bulkhandler", "calendar", 
    "callback", "callforward", "callrecording", "callwaiting", "campon", "cdr", "cel", "certman", "cidlookup", 
    "conferences", "contactmanager", "customappsreg", "cxpanel", "dahdiconfig", "dashboard", "daynight", "dictate", 
    "digium_phones", "digiumaddoninstaller", "directory", "disa", "donotdisturb", "dundicheck", "extensionsettings", 
    "fax", "featurecodeadmin", "findmefollow", "firewall", "framework", "fw_langpacks", "hotelwakeup", "iaxsettings", 
    "infoservices", "ivr", "logfiles", "manager", "miscapps", "miscdests", "motif", "music", "outroutemsg", "paging", 
    "parking", "pbdirectory", "phonebook", "pinsets", "presencestate", "printextensions", "queueprio", "queues", 
    "recordings", "restart", "ringgroups", "setcid", "sipsettings", "soundlang", "speeddial", "superfecta", 
    "timeconditons", "tts", "ttsengines", "ucp", "userman", "vmblast", "voicemail", "weakpasswords", "webrtc", "xmpp"
]

# Base URL and save directory
base_url = "https://weblate.sangoma.com/download/freepbx/{}/pl/po/"
tmp_dir = "/tmp/translations/"
target_dir_base = "/var/www/html/admin/modules/{}/i18n/pl_PL/LC_MESSAGES/"

# Ensure the temporary directory exists
if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)

def download_translation(module_name):
    try:
        url = base_url.format(module_name)
        response = requests.get(url, allow_redirects=True)

        if response.status_code == 200:
            tmp_file_path = os.path.join(tmp_dir, f"{module_name}.pl")
            with open(tmp_file_path, 'wb') as file:
                file.write(response.content)
            logging.info(f"Downloaded translation for {module_name}")
            return tmp_file_path
        elif response.status_code == 404:
            logging.warning(f"No translation found for {module_name}")
        else:
            logging.error(f"Failed to download {module_name}: Status Code {response.status_code}")
    except Exception as e:
        logging.error(f"Error downloading {module_name}: {e}")

def process_translation(module_name, tmp_file_path):
    target_dir = target_dir_base.format(module_name)
    target_po_file_path = os.path.join(target_dir, f"{module_name}.po")
    target_mo_file_path = os.path.join(target_dir, f"{module_name}.mo")

    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Copy the .pl file to .po
    shutil.copy(tmp_file_path, target_po_file_path)
    logging.info(f"Copied translation to {target_po_file_path}")

    # Run msgfmt to generate .mo file
    subprocess.run(["msgfmt", "-v", target_po_file_path, "-o", target_mo_file_path])
    logging.info(f"Processed .po to .mo for {module_name}")

for module in modules:
    logging.info(f"Processing {module}...")
    tmp_file_path = download_translation(module)
    if tmp_file_path:
        process_translation(module, tmp_file_path)

# Run fwconsole chown after processing all files
subprocess.run(["fwconsole", "chown"])
logging.info("Ran fwconsole chown command")
