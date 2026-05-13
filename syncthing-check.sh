#!/usr/bin/env bash
# ~/.config/scripts/syncthing-check.sh
if ! systemctl --user is-active --quiet syncthing; then
    notify-send -u normal "Syncthing" "Not running — start with: systemctl --user start syncthing"
fi
