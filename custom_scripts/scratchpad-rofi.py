#!/usr/bin/env python3
import i3ipc
import subprocess

def get_scratchpad_windows():
    i3 = i3ipc.Connection()
    windows = i3.get_tree().scratchpad().leaves()
    return sorted(windows, key=lambda x: x.name or "")

def rofi_select(windows):
    if not windows:
        subprocess.run(["notify-send", "Scratchpad", "No scratchpad windows"])
        return None

    # формируем подписи вида: [Class] Title
    options = []
    lookup = {}

    for w in windows:
        cls = w.window_class or "unknown"
        title = w.name or "no title"
        label = f"[{cls}] {title}"
        options.append(label)
        lookup[label] = w

    rofi_input = "\n".join(options).encode()

    result = subprocess.run(
        ["rofi", "-dmenu", "-i", "-p", "Scratchpad"],
        input=rofi_input,
        stdout=subprocess.PIPE
    )
    choice = result.stdout.decode().strip()
    return lookup.get(choice)

def focus_scratchpad_window(window):
    if window:
        window.command("scratchpad show")
        window.command("focus")

def main():
    windows = get_scratchpad_windows()
    selected = rofi_select(windows)
    focus_scratchpad_window(selected)

if __name__ == "__main__":
    main()
