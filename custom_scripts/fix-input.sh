#!/bin/bash

setxkbmap -layout us,ru -option grp:caps_toggle
xset r rate 500 50
for id in $(xinput list --id-only); do
    if xinput list-props "$id" | grep -q "libinput Accel Speed"; then
        xinput --set-prop "$id" "libinput Accel Profile Enabled" 0 1 0
        xinput --set-prop "$id" "libinput Accel Speed" 0.5
    fi
done
