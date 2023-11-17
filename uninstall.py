import os
import shutil

# List of modules for which language files were installed
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

# Base directory for language files
base_dir = "/var/www/html/admin/modules/"

def uninstall_translation(module_name):
    try:
        target_dir = os.path.join(base_dir, module_name, "i18n/pl_PL/LC_MESSAGES")
        if os.path.exists(target_dir):
            po_file_path = os.path.join(target_dir, f"{module_name}.po")
            mo_file_path = os.path.join(target_dir, f"{module_name}.mo")

            # Remove .po and .mo files
            if os.path.exists(po_file_path):
                os.remove(po_file_path)
            if os.path.exists(mo_file_path):
                os.remove(mo_file_path)

            print(f"Uninstalled translation for {module_name}")
        else:
            print(f"No translation directory found for {module_name}")
    except Exception as e:
        print(f"Error uninstalling translation for {module_name}: {e}")

# Uninstall translations for each module
for module in modules:
    print(f"Uninstalling translation for {module}...")
    uninstall_translation(module)

print("Uninstallation of language files completed.")
