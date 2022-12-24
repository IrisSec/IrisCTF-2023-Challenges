#!/bin/bash

(&>/dev/null python3 /home/user/chal_serv.py)&

python3 /home/user/chal.py 2>&1
