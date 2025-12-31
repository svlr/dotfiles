#!/usr/bin/env python3

import shutil
import subprocess
from pathlib import Path

# Paths
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


# User confirmation
def ask_user(prompt: str) -> bool:
    while True:
        ans = input(prompt).strip().lower()
        if ans == "y":
            return True
        elif ans == "n":
            return False
        print("Invalid input. Please enter y or n.")


# Backup
def backup_configs():
    print("\nCreating backup of existing configuration files...")
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    # Backup .zshrc and .xprofile
    for file in [ZSHRC, XPROFILE]:
        if file.exists():
            dest = BACKUP_DIR / file.name
            print(f"Backing up {file} -> {dest}")
            shutil.copy2(file, dest)

    # Backup directories from ~/.config
    for item in CONFIGS_DIR.iterdir():
        if item.name in EXCLUDE_FILES or not item.is_dir():
            continue
        target_path = CONFIG_TARGET / item.name
        if target_path.exists():
            dest = BACKUP_DIR / ".config" / item.name
            print(f"Backing up {target_path} -> {dest}")
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(target_path, dest, dirs_exist_ok=True)

    print("Backup completed.\n")


# Oh My Zsh check and install
def oh_my_zsh_installed() -> bool:
    return ZSHRC.exists() and "oh-my-zsh" in ZSHRC.read_text()


def install_oh_my_zsh():
    print("Installing Oh My Zsh...")
    cmd = (
        f'sh -c "$(wget -qO- {OH_MY_ZSH_INSTALLER})" "" '
        "--unattended --skip-chsh --keep-zshrc"
    )
    subprocess.run(cmd, shell=True, check=True)

    with open("/etc/shells", "r") as f:
        shells = [
            line.strip() for line in f if line.strip() and not line.startswith("#")
        ]

    zsh_path = next((s for s in shells if s.endswith("/zsh")), None)
    if zsh_path:
        subprocess.run(f"chsh -s {zsh_path}", shell=True, check=True)
        print(f"Default shell set to {zsh_path}.")
    else:
        print("Warning: zsh was not found in /etc/shells. chsh was not executed.")


# Install configs
def install_configs():
    print("\nInstalling configuration files...\n")

    if not oh_my_zsh_installed():
        install_oh_my_zsh()
    else:
        print("Oh My Zsh is already installed. Skipping.\n")

    # Copy .zshrc and .xprofile
    for name in [".zshrc", ".xprofile"]:
        src = CONFIGS_DIR / name
        dest = HOME / name
        if src.exists():
            print(f"Copying {name} -> {dest}")
            shutil.copy(src, dest)

    # Copy directories to ~/.config
    for item in CONFIGS_DIR.iterdir():
        if item.name in EXCLUDE_FILES or item.name in {".zshrc", ".xprofile"}:
            continue
        if item.is_dir():
            dest = CONFIG_TARGET / item.name
            print(f"Copying directory {item.name} -> {dest}")
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)

    print("\nConfiguration files installed.\n")


# Install custom scripts
def install_scripts():
    print("\nInstalling custom scripts...\n")
    SCRIPT_TARGET.mkdir(parents=True, exist_ok=True)

    for script in CUSTOM_SCRIPTS_DIR.iterdir():
        if script.name in EXCLUDE_FILES or not script.is_file():
            continue
        dest = SCRIPT_TARGET / script.name
        print(f"Copying {script.name} -> {dest}")
        shutil.copy(script, dest)
        dest.chmod(0o755)

    print("\nCustom scripts installed.")


# Install wallpapers
def install_wallpapers():
    print("\nInstalling wallpapers...\n")
    WALL_TARGET.mkdir(parents=True, exist_ok=True)

    for wallpaper in WALLPAPER_DIR.iterdir():
        if wallpaper.name in EXCLUDE_FILES or not wallpaper.is_file():
            continue
        dest = WALL_TARGET / wallpaper.name
        print(f"Copying {wallpaper.name} -> {dest}")
        shutil.copy(wallpaper, dest)

    print("\nWallpapers installed.")


# Main
def main():
    if ask_user(
        "This will overwrite configuration files in ~/.config, .zshrc and .xprofile. "
        "Create a backup and continue? (y/n): "
    ):
        backup_configs()
        install_configs()
    else:
        print("Configuration installation cancelled.")

    if ask_user(
        "Install custom scripts to ~/MyFiles/usefull_scripts? "
        "(This does not affect the system) (y/n): "
    ):
        install_scripts()
    else:
        print("Custom scripts installation skipped.")

    if ask_user(
        "Install wallpapers from ./wallpapers to ~/MyFiles/wallpapers? (y/n): "
    ):
        install_wallpapers()
    else:
        print("Wallpaper installation skipped.")


if __name__ == "__main__":
    main()
