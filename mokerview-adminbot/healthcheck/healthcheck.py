#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from pwn import *

r = remote("127.0.0.1", 1337)
print(r.recvuntil(b'== proof-of-work: '))
exit (0)
