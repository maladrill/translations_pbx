import requests
import os

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

# Base URL for downloading the translations
base_url = "https://weblate.sangoma.com/download/freepbx/{}/pl/mo/"

# Directory to save the translations
save_dir = "/tmp/translations/"

# Create the directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Function to download and save the translation file for a module
def download_translation(module_name):
    try:
        # Construct the URL
        url = base_url.format(module_name)
        response = requests.get(url, allow_redirects=True)

        # Check if the request was successful
        if response.status_code == 200:
            # Save the file
            file_path = os.path.join(save_dir, f"{module_name}.mo")
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return f"Downloaded translation for {module_name}"
        else:
            return f"Failed to download translation for {module_name}: Status Code {response.status_code}"
    except Exception as e:
        return f"An error occurred while downloading translation for {module_name}: {str(e)}"

# Download translations for all modules
download_results = [download_translation(module) for module in modules]
download_results
