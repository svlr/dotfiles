#!/usr/bin/env bash
set -euo pipefail

echo "Checking if chaotic-aur is configured..."

if ! grep -q "^\[chaotic-aur\]" /etc/pacman.conf; then
    echo "chaotic-aur not found. Adding repository..."

    sudo pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com
    sudo pacman-key --lsign-key 3056513887B78AEB

    sudo pacman -U --noconfirm \
        https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst
    sudo pacman -U --noconfirm \
        https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst

    echo
    echo "[chaotic-aur]" | sudo tee -a /etc/pacman.conf >/dev/null
    echo "Include = /etc/pacman.d/chaotic-mirrorlist" | sudo tee -a /etc/pacman.conf >/dev/null

    echo "Updating system packages..."
    sudo pacman -Syu --noconfirm
else
    echo "chaotic-aur is already configured."
fi

echo "Checking if yay is installed..."
if ! command -v yay >/dev/null 2>&1; then
    echo "Installing yay..."
    sudo pacman -S --noconfirm yay
else
    echo "yay is already installed."
fi

echo "Ensuring Python is installed..."
sudo pacman -S --noconfirm python

echo "Running dependency installation..."
python3 install_packages.py

echo "Installing dotfiles, scripts and wallpapers..."
python3 install_dotfiles.py

echo "Installation finished."
