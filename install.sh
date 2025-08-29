#!/bin/bash

set -e

YAY=$(command -v yay || true)

if [[ -z "$YAY" ]]; then
  echo "[*] yay не найден, начинаю установку..."

  echo "[*] Добавляю ключ Chaotic AUR"
  sudo pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com
  sudo pacman-key --lsign-key 3056513887B78AEB

  echo "[*] Устанавливаю chaotic-keyring и mirrorlist"
  sudo pacman -U --noconfirm \
    'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' \
    'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'

  echo "[*] Проверяю наличие chaotic-aur в pacman.conf"
  if ! grep -q "\[chaotic-aur\]" /etc/pacman.conf; then
    echo "[*] Добавляю chaotic-aur в /etc/pacman.conf"
    echo -e "\n[chaotic-aur]\nInclude = /etc/pacman.d/chaotic-mirrorlist" | sudo tee -a /etc/pacman.conf
  fi

  echo "[*] Обновляю систему и ставлю yay"
  sudo pacman -Syu --noconfirm
  sudo pacman -S --noconfirm yay
else
  echo "[✓] yay уже установлен"
fi

echo "[*] Запускаю install.py"
python3 install.py

echo "[*] Запускаю setup.py"
#python3 setup.py

echo "[✓] Полная установка завершена. Аллаху Акбар."
