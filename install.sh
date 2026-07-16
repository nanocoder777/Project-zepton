#!/data/data/com.termux/files/usr/bin/bash
# Zepton installer for Termux.
set -e

echo "[*] Updating package lists..."
pkg update -y

echo "[*] Installing Python and Git..."
pkg install -y python git

read -r -p "[?] Install Metasploit? (payloads + handlers) [y/N] " msf
if [ "$msf" = "y" ] || [ "$msf" = "Y" ]; then
    pkg install -y metasploit || {
        echo "[!] Metasploit not in your repos — try: pkg install tur-repo && pkg install metasploit"
    }
fi

read -r -p "[?] Install android-tools (adb/fastboot)? [y/N] " adb
if [ "$adb" = "y" ] || [ "$adb" = "Y" ]; then
    pkg install -y android-tools
fi

echo "[+] Done. Launch with: python zepton.py"
