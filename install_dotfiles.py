#!/usr/bin/env python3

import shutil
import subprocess
from pathlib import Path

# Пути
REPO_DIR = Path.cwd()
CONFIGS_DIR = REPO_DIR / "configs"
CUSTOM_SCRIPTS_DIR = REPO_DIR / "custom_scripts"
WALLPAPER_DIR = REPO_DIR / "wallpapers"

HOME = Path.home()
CONFIG_TARGET = HOME / ".config"
SCRIPT_TARGET = HOME / "MyFiles" / "usefull_scripts"
WALL_TARGET = HOME / "MyFiles" / "wallpapers"
BACKUP_DIR = HOME / "dotfiles_backup"

EXCLUDE_FILES = {"usage.txt"}
ZSHRC = HOME / ".zshrc"
XPROFILE = HOME / ".xprofile"

OH_MY_ZSH_INSTALLER = (
    "https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh"
)


# Подтверждение
def ask_user(prompt: str) -> bool:
    while True:
        ans = input(prompt).strip().lower()
        if ans == "y":
            return True
        elif ans == "n":
            return False
        print("🚫 Введите y или n.")


# Бэкап
def backup_configs():
    print("\n💾 Делаю резервную копию старых конфигов...")
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    # Бэкап .zshrc и .xprofile
    for file in [ZSHRC, XPROFILE]:
        if file.exists():
            dest = BACKUP_DIR / file.name
            print(f"→ Бэкап {file} → {dest}")
            shutil.copy2(file, dest)

    # Бэкап каталогов из ~/.config
    for item in CONFIGS_DIR.iterdir():
        if item.name in EXCLUDE_FILES or not item.is_dir():
            continue
        target_path = CONFIG_TARGET / item.name
        if target_path.exists():
            dest = BACKUP_DIR / ".config" / item.name
            print(f"→ Бэкап {target_path} → {dest}")
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(target_path, dest, dirs_exist_ok=True)

    print("✅ Бэкап завершён.\n")


# Проверка и установка Oh My Zsh
def oh_my_zsh_installed() -> bool:
    return ZSHRC.exists() and "oh-my-zsh" in ZSHRC.read_text()


def install_oh_my_zsh():
    print("→ Устанавливаю Oh My Zsh...")
    cmd = (
        f'sh -c "$(wget -qO- {OH_MY_ZSH_INSTALLER})" "" '
        "--unattended --skip-chsh --keep-zshrc"
    )
    subprocess.run(cmd, shell=True, check=True)

    zsh_path = subprocess.run(
        "which zsh", shell=True, capture_output=True, text=True
    ).stdout.strip()
    subprocess.run(f"chsh -s {zsh_path}", shell=True, check=True)
    print("→ Oh My Zsh установлен, zsh установлен как shell по умолчанию.\n")


# Установка конфигов
def install_configs():
    print("\n📂 Установка конфигов...\n")

    if not oh_my_zsh_installed():
        install_oh_my_zsh()
    else:
        print("→ Oh My Zsh уже установлен, пропускаю установку.\n")

    # Копирование .zshrc и .xprofile
    for name in [".zshrc", ".xprofile"]:
        src = CONFIGS_DIR / name
        dest = HOME / name
        if src.exists():
            print(f"→ Копирую {name} → {dest}")
            shutil.copy(src, dest)

    # Копирование директорий в ~/.config
    for item in CONFIGS_DIR.iterdir():
        if item.name in EXCLUDE_FILES or item.name in {".zshrc", ".xprofile"}:
            continue
        if item.is_dir():
            dest = CONFIG_TARGET / item.name
            print(f"→ Копирую директорию {item.name} → {dest}")
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)

    print("\n✅ Конфиги установлены.\n")


# Установка скриптов
def install_scripts():
    print("\n📂 Установка кастомных скриптов...\n")
    SCRIPT_TARGET.mkdir(parents=True, exist_ok=True)

    for script in CUSTOM_SCRIPTS_DIR.iterdir():
        if script.name in EXCLUDE_FILES or not script.is_file():
            continue
        dest = SCRIPT_TARGET / script.name
        print(f"→ Копирую {script.name} → {dest}")
        shutil.copy(script, dest)
        dest.chmod(0o755)

    print("\n✅ Кастомные скрипты установлены.")


# Установка обоев
def install_wallpapers():
    print("\n🖼️  Установка обоев...\n")
    WALL_TARGET.mkdir(parents=True, exist_ok=True)

    for wallpaper in WALLPAPER_DIR.iterdir():
        if wallpaper.name in EXCLUDE_FILES or not wallpaper.is_file():
            continue
        dest = WALL_TARGET / wallpaper.name
        print(f"→ Копирую {wallpaper.name} → {dest}")
        shutil.copy(wallpaper, dest)

    print("\n✅ Обои установлены.")


# Главный запуск
def main():
    if ask_user(
        "⚠️  Это перезапишет ваши конфиги в ~/.config, .zshrc и .xprofile. Сделать бэкап и продолжить? (y/n): "
    ):
        backup_configs()
        install_configs()
    else:
        print("🚫 Установка конфигов отменена.")

    if ask_user(
        "ℹ️  Установить кастомные скрипты в ~/MyFiles/usefull_scripts? (Это не влияет на систему) (y/n): "
    ):
        install_scripts()
    else:
        print("🕳️  Установка скриптов пропущена.")

    if ask_user("🌄 Установить обои из wallpapers в ~/MyFiles/wallpapers? (y/n): "):
        install_wallpapers()
    else:
        print("🕳️  Установка обоев пропущена.")


if __name__ == "__main__":
    main()
