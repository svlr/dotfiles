#!/bin/bash
# id мышки
MOUSE_ID=9

# Ставим flat профиль и скорость 0.5
xinput --set-prop $MOUSE_ID "libinput Accel Profile Enabled" 0 1 0
xinput --set-prop $MOUSE_ID "libinput Accel Speed" 0.5

