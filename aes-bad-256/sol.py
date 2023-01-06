from pwn import *

while True:
    r = remote("aes.chal.irisc.tf", 10100)

    mapped = []
    bz = 16

    r.recvuntil(b"> ")
    r.sendline(b"1")
    r.recvuntil(b"> ")
    r.sendline(b"aaaaaa")
    cmd = r.recvuntil(b"> ").decode().split("\n")[-7]

    flag = "flag".encode()
    flag2 = "FLAG".encode()
    echo = "echo".encode()
    mapped = [-1, -1, -1, -1]

    for i in range(bz):
        done = False
        i = i * 32
        for c in "123":
            if done: break
            nc = c if cmd[i] != c else "0"
            new_cmd = cmd[:i] + nc + cmd[i+1:]
            r.sendline(b"2")
            #r.recvuntil(b"(hex) > ")
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

    print(mapped)
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
                    exit()
                if b"..." not in b:
                    continue
                b = b.split(b"...")[0][-4:]
                if b[affects] == flag[affects] or b[affects] == flag2[affects]:
                    cmd = new_cmd
                    done = True
                    break

    r.close()
