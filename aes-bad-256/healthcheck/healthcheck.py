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

while True:
    r = pwnlib.tubes.remote.remote('127.0.0.1', 1337)
    print(r.recvuntil(b'== proof-of-work: '))
    if r.recvline().startswith(b'enabled'):
        handle_pow(r)

    mapped = []
    bz = 16

    r.recvuntil(b"> ")
    r.sendline(b"1")
    r.recvuntil(b"> ")
    r.sendline(b"aaaaaa")
    cmd = r.recvuntil(b"> ").decode().split("\n")[-7]

    flag = "flag".encode()
    echo = "echo".encode()
    mapped = [-1, -1, -1, -1]

    for i in range(bz):
        done = False
        i = i * 16
        for c in "0123":
            if done: break
            nc = c if cmd[i] != c else "0"
            new_cmd = cmd[:i] + nc + cmd[i+1:]
            r.sendline(b"2")
            r.recvuntil(b"(hex) > ")
            r.sendline(new_cmd.encode())
            d = r.recvuntil(b"1. Get")
            if b"Unknown command" in d:
                d = d.split(b"...")[0][-4:]
                dc = 0
                dl = 0
                for j in range(4):
                    if d[j] != echo[j]:
                        dc += 1
                        dl = j
                if dc == 1:
                    mapped[dl] = i
                    done = True
                    break

    # print(mapped)
    if any(i == -1 for i in mapped):
        r.close()
        continue

    # brute force char matching flag
    for affects, i in enumerate(mapped):
        done = False
        for c1 in range(256):
            if done: break
            for c2 in range(256):
                c = bytes([c1, c2])
                r.sendline(b"2")
                r.recvuntil(b"(hex) > ")
                new_cmd = cmd[:i] + c.hex() + cmd[i+4:]
                r.sendline(new_cmd.encode())
                b = r.recvuntil(b"1. Get")
                if b"irisctf" in b:
                    print(b)
                    exit(0)
                if b"..." not in b:
                    continue
                b = b.split(b"...")[0][-4:]
                if b[affects] == flag[affects]:
                    cmd = new_cmd
                    done = True
                    break

    r.close()

exit(-1)
