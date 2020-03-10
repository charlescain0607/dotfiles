#!/usr/bin/env bash

# terminate already running bar instances
killall -q polybar

# launch bar
polybar example &

echo "Bars launched..."
