import os
import subprocess
import json
from base64 import urlsafe_b64encode as b64encode

BANNER = """

Welcome to my insecure temporary data service!
1) Write data
2) Read data

"""

REMOTE = "http://0:25566/"

def check(url):
    return json.loads(subprocess.check_output(["curl", "-s", url]))

print(BANNER)
while True:
    choice = input("> ")
    try:
        print(check("http://flag_domain:25566/flag"))
    except subprocess.CalledProcessError: pass
    try:
        if choice == '1':
            env = input("Name? ")
            if check(REMOTE + "env?q=" + b64encode(env.encode()).decode())["ok"]:
                os.environ[env] = input("Value? ")
            else:
                print("No!")
        elif choice == '2':
            env = input("Name? ")
            if check(REMOTE + "env?q=" + b64encode(env.encode()).decode())["ok"]:
                if env in os.environ:
                    print(os.environ[env])
                else:
                    print("(Does not exist)")
            else:
                print("No!")
        else:
            print("Bye!")
            exit()

    except Exception as e:
        print(e)
        exit()
