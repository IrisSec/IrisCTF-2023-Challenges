import subprocess
import time
import sys

print("I will run your program in my example jail. Give it to me in hex. Write 'DONE' when you are done.")
print("Make sure to send a newline every <4096 bytes because of input buffering.")
print("Compile the program using the given dockerfile image!")
sys.stdout.flush()

read = ""
while "DONE" not in read:
    read += sys.stdin.read(1)

print("Got it.")

read = read.replace("DONE", "").replace("\n", "")

solve = bytes.fromhex(read)

with open("/tmp/solve", "wb") as f:
    f.write(solve)

subprocess.check_output(["chmod", "+x", "/tmp/solve"])

p = subprocess.Popen(["socat", "-", "exec:\"bash -i\",pty,stderr,setsid,sigint,sane"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
p.stdin.write(b"nsjail --config /nsjail.cfg &\n")

time.sleep(5)

print(p.communicate(timeout=3)[0].decode())
