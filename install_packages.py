#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys

# === CONSTANTS === #
PKG_FILE = Path("packages.txt")


def fail(message: str):
    """Выводит сообщение об ошибке и завершает программу."""
    print(f"[!] Ошибка: {message}")
    sys.exit(1)


def get_required_packages() -> list:
    """Считывает список пакетов из файла packages.txt, исключая комментарии и пустые строки."""
    try:
        with open(PKG_FILE, "r", encoding="utf-8") as f:
            return [
                line.strip()
                for line in f
                if line.strip() and not line.strip().startswith("#")
            ]
    except FileNotFoundError:
        fail("Файл packages.txt не найден!")


def is_package_installed(pkg: str) -> bool:
    """Проверяет, установлен ли пакет через yay -Qi <pkg>."""
    result = subprocess.run(
        ["yay", "-Qi", pkg],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def get_missing_packages(required: list) -> list:
    """Возвращает список пакетов, которые не установлены в системе."""
    return [pkg for pkg in required if not is_package_installed(pkg)]


def prompt_yes_no(prompt: str) -> bool:
    """Универсальный ввод подтверждения y/n"""
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("🚫 Введите 'y' или 'n'.")


def install_packages(packages: list):
    """Устанавливает список пакетов через yay."""
    result = subprocess.run(["yay", "-S", "--needed", "--noconfirm"] + packages)
    if result.returncode != 0:
        fail("Ошибка при установке пакетов через yay.")
    print("\n[✓] Установка завершена!")


def main():
    print("[*] Загружаю список зависимостей из packages.txt...")
    required_packages = get_required_packages()
    print(f"[+] Требуемых пакетов: {len(required_packages)}")

    print("[*] Определяю, какие пакеты нужно установить...")
    missing = get_missing_packages(required_packages)
    print(f"[+] Недостающих пакетов: {len(missing)}")

    if not missing:
        print("[✓] Все необходимые пакеты уже установлены.")
        return

    print("\n📦 К установке подготовлены следующие пакеты:\n")
    for pkg in missing:
        print(f" - {pkg}")
    print()

    if prompt_yes_no("✅ Установить недостающие пакеты?"):
        install_packages(missing)
    else:
        print("🚫 Установка отменена пользователем.")


if __name__ == "__main__":
    main()
