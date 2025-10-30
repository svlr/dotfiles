#!/bin/bash

set -e

echo "🔧 Проверяю наличие chaotic-aur..."

if ! grep -q "\[chaotic-aur\]" /etc/pacman.conf; then
    echo "⚙️ Добавляю репозиторий chaotic-aur..."

    sudo pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com
    sudo pacman-key --lsign-key 3056513887B78AEB

    sudo pacman -U --noconfirm 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst'
    sudo pacman -U --noconfirm 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'

    echo -e "\n[chaotic-aur]\nInclude = /etc/pacman.d/chaotic-mirrorlist" | sudo tee -a /etc/pacman.conf

    echo "📦 Обновляю систему с новым зеркалом chaotic-aur..."
    sudo pacman -Syu --noconfirm
else
    echo "✅ chaotic-aur уже подключён."
fi

echo "🔍 Проверяю наличие yay..."
if ! command -v yay >/dev/null 2>&1; then
    echo "⚙️ Устанавливаю yay..."
    sudo pacman -S --noconfirm yay
else
    echo "✅ yay уже установлен."
fi

echo "⚙️ Устанавливаю python..."
sudo pacman -S python

echo "🚀 Запускаю установку зависимостей..."
python3 install_packages.py

echo "🎛️ Запускаю установку конфигов, скриптов и обоев..."
python3 install_dotfiles.py

echo "✅ Установка завершена!"
