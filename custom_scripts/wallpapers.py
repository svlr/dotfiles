#!/usr/bin/env python3
import os
import random
import subprocess

WALLPAPER_DIR = os.path.expanduser("~/MyFiles/wallpapers")
all_pics = [
    os.path.join(WALLPAPER_DIR, f)
    for f in os.listdir(WALLPAPER_DIR)
    if f.lower().endswith((".jpg", ".png"))
]

chosen_pic = random.choice(all_pics)
subprocess.run(["feh", "--bg-fill", chosen_pic])
