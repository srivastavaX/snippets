#!/usr/bin/env python3
import subprocess
from pathlib import Path
import sys

# Path to your dotfiles repository
DOTFILES_DIR = Path.home() / "repos/dotfiles"  # Adjust here
TARGET_DIR = Path.home()

def stow_package(package_path: Path, action: str):
    """Stow or unstow a single package."""
    print(f"{action.capitalize()}ing package: {package_path.name}")
    
    cmd = ["stow", "-t", str(TARGET_DIR)]
    if action == "unstow":
        cmd.insert(1, "-D")
    cmd.append(package_path.name)
    
    subprocess.run(cmd, cwd=DOTFILES_DIR, check=True)

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("stow", "unstow"):
        print(f"Usage: {sys.argv[0]} [stow|unstow]")
        sys.exit(1)

    action = sys.argv[1]

    if not DOTFILES_DIR.exists():
        print(f"Error: dotfiles directory {DOTFILES_DIR} does not exist.")
        sys.exit(1)

    packages = [p for p in DOTFILES_DIR.iterdir() if p.is_dir()]
    if not packages:
        print("No packages found in dotfiles directory.")
        return

    for package in packages:
        stow_package(package, action)

    print(f"All packages {action}ed successfully.")

if __name__ == "__main__":
    main()
