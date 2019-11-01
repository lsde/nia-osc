#!/bin/bash
cd $(dirname "$0")
while true; do
    venv/bin/python3 nia-osc.py $@
done
