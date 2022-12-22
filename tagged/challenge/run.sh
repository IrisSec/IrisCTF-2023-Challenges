#!/bin/sh
cd /home/user
python3 -m gunicorn -b 0.0.0.0:1337 "chal:app" >/dev/null 2>/dev/null
