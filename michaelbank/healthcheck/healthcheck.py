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

r = pwnlib.tubes.remote.remote('127.0.0.1', 1337)
print(r.recvuntil(b'== proof-of-work: '))
if r.recvline().startswith(b'enabled'):
    handle_pow(r)

r.sendline(b"1\na\na\n2\na\na\n6\n5\nmichael")
r.sendline(b"1\nb\nb\n2\nb\nb\n6\n5\nmichael")
r.sendline(b"2\nbob\nbob\n6\n25.35\nmichael")
r.sendline(b"5\ntr\n1\nmIchael\na\n2\nmichael\na")
r.sendline(b"5\nus\n3")

print(r.recvuntil(b'irisctf{'))
print(r.recvuntil(b'}'))

exit(0)
