#!/bin/bash

# Kill existing polybar instances
pkill -x polybar

# Wait until they're fully terminated
while pgrep -x polybar >/dev/null; do sleep 0.1; done

# Define monitors
MAIN=HDMI-A-0
SIDE=HDMI-1

# Launch bars
MONITOR=$MAIN polybar topbar &
MONITOR=$SIDE polybar sidepanel &
