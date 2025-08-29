#!/usr/bin/env python3
from i3ipc import Connection, Event

i3 = Connection()

def handle_window_event(i3, e):
    if e.container.window_class == "steam":
        # Главное окно
        if e.container.name == "Steam":
            e.container.command("floating disable")
        else:
            e.container.command("floating enable")

i3.on(Event.WINDOW_FOCUS, handle_window_event)
i3.on(Event.WINDOW_NEW, handle_window_event)
i3.on(Event.WINDOW_TITLE, handle_window_event)

i3.main()

