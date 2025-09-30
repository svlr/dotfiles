#!/bin/bash

# Kill existing bars
pkill -x polybar

# Wait until polybar processes are gone
while pgrep -x polybar >/dev/null; do sleep 0.1; done

# Start main bar
MONITOR=$(xrandr --query | grep " connected" | cut -d" " -f1 | head -n1)
MONITOR=$MONITOR polybar mybar &

