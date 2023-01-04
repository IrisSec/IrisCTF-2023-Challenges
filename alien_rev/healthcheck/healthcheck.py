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

def decode_alien(s: str):
    s = (s.replace("・┤┤╙", "0")
        .replace("・├┴╗╬", "1")
        .replace("・╝└┤┐┼", "2")
        .replace("・┬╒┘─└┴", "3")
        .replace("・├╡┌└┬╥", "4")
        .replace("・┴┐┤┬", "5")
        .replace("・└─┐┤─┴┴", "6")
        .replace("・┬╧─┘╣┐", "7"))
    
    s = s[::-1]
    num = int(s, 8)
    return num

def encode_alien(num: int):
    s = oct(num).replace("0o", "")
    s = s[::-1]

    s = (s.replace("0", "・┤┤╙")
        .replace("1", "・├┴╗╬")
        .replace("2", "・╝└┤┐┼")
        .replace("3", "・┬╒┘─└┴")
        .replace("4", "・├╡┌└┬╥")
        .replace("5", "・┴┐┤┬")
        .replace("6", "・└─┐┤─┴┴")
        .replace("7", "・┬╧─┘╣┐")
        .replace("-", "・─"))
    
    if "o" in s:
        print("BRUH WHY IS o in s???? " + str(num))
        exit(0)

    return s

def solve_operation(a:int, b:int, op:str):
    if op == "╞└╠╤├┼│":
        return a - b
    elif op == "──╖┴╚┬╜═┴└╪┤┤":
        return a ^ b
    elif op == "┘└└┼┤┐╤┘┤┤╜":
        return (b * 3) // a
    elif op == "─╦╗┘└╙":
        return (a * 3) % (b * 3)
    elif op == "┘┘│┬╖├":
        return a * a + b
    elif op == "┼└╧╛╪╝╚│┴":
        return 2*a - 2*b
    else:
        raise Exception("operation not supported")

for i in range(68):
    r.recvuntil(" ┴┘╟│ ".encode("utf-8")).decode("utf-8")

    question_str = r.recvline().decode("utf-8")
    question_split = question_str.split(" ")
    print(question_str[:-1])
    a = decode_alien(question_split[0])
    b = decode_alien(question_split[2][:-2])
    operation = question_split[1]
    result = solve_operation(a, b, operation)

    print(f"{a} {operation} {b} = {result} ({encode_alien(result)})")
    print("")

    result_bytes = (encode_alien(result) + "\n").encode("utf-8")

    r.send(result_bytes)

print(r.read().decode("utf-8"))