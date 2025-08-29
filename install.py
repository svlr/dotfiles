#!/usr/bin/env python3

import subprocess
import sys


def fail(msg):
    print(f"[!] Ошибка: {msg}")
    sys.exit(1)


print("[*] Проверяю наличие yay...")
yay_check = subprocess.run(["which", "yay"], capture_output=True, text=True)
if yay_check.returncode != 0:
    fail("yay не найден. Установи его сначала!")

print("[*] Сканирую установленные пакеты (через yay)...")
result = subprocess.run(["yay", "-Qq"], capture_output=True, text=True)
installed_packages = []
for line in result.stdout.splitlines():
    if line.strip():
        installed_packages.append(line.strip())

print(f"[+] Установленных пакетов: {len(installed_packages)}")

print("[*] Загружаю packages.txt...")
required_packages = []
try:
    with open("packages.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                required_packages.append(line)
except FileNotFoundError:
    fail("Файл packages.txt не найден!")

print(f"[+] Требуемых пакетов: {len(required_packages)}")

print("[*] Сравниваю списки...")
missing_packages = []
for pkg in required_packages:
    if pkg not in installed_packages:
        missing_packages.append(pkg)

print(f"[+] Недостающих пакетов: {len(missing_packages)}")

if not missing_packages:
    print("[✓] Всё уже установлено. Алхамдулиллях!")
    sys.exit(0)

print("[*] Устанавливаю недостающие пакеты через yay...")
subprocess.run(["yay", "-S", "--needed", "--noconfirm"] + missing_packages)

print("[✓] Установка завершена! Машалла.")
