#!/bin/sh
cd /home/user
# waitress to share state easily :))))
python3 -m waitress --host 0.0.0.0 --port 1337 --no-expose-tracebacks "chal:app" 2>/dev/null 1>/dev/null
