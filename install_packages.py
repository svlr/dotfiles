#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys

PKG_FILE = Path("packages.txt")


def fail(message: str):
    print(f"[ERROR] {message}")
    sys.exit(1)


def get_required_packages() -> list:
    try:
        with open(PKG_FILE, "r", encoding="utf-8") as f:
            return [
                line.strip()
                for line in f
                if line.strip() and not line.strip().startswith("#")
            ]
    except FileNotFoundError:
        fail("packages.txt file not found.")


def is_package_installed(pkg: str) -> bool:
    result = subprocess.run(
        ["yay", "-Qi", pkg],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def get_missing_packages(required: list) -> list:
    return [pkg for pkg in required if not is_package_installed(pkg)]


def prompt_yes_no(prompt: str) -> bool:
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def install_packages(packages: list):
    try:
        subprocess.run(["yay", "-S", "--needed"] + packages, check=True)
        print("\n[SUCCESS] Package installation completed.")
    except subprocess.CalledProcessError:
        print("\n[WARNING] A conflict occurred during package installation.")
        print(
            "Please resolve conflicting packages manually and run the script again."
        )
        sys.exit(1)


def main():
    print("[INFO] Loading dependency list from packages.txt...")
    required_packages = get_required_packages()
    print(f"[INFO] Total required packages: {len(required_packages)}")

    print("[INFO] Checking for missing packages...")
    missing = get_missing_packages(required_packages)
    print(f"[INFO] Missing packages: {len(missing)}")

    if not missing:
        print("[OK] All required packages are already installed.")
        return

    print("\nThe following packages will be installed:\n")
    for pkg in missing:
        print(f" - {pkg}")
    print()

    if prompt_yes_no("Install missing packages?"):
        install_packages(missing)
    else:
        print("Installation cancelled by user.")


if __name__ == "__main__":
    main()
