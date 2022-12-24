from flask import Flask, request
import string
from base64 import urlsafe_b64decode as b64decode

app = Flask(__name__)

BAD_ENV = ["LD", "LC", "PATH", "ORIGIN"]

@app.route("/env")
def env():
    data = b64decode(request.args['q']).decode()
    print(data)
    if any(c in data.upper() for c in BAD_ENV) \
            or any(c not in string.printable for c in data):
        return {"ok": 0}
    return {"ok": 1}

@app.route("/flag")
def flag():
    with open("flag", "r") as f:
        flag = f.read()
    return {"flag": flag}

app.run(port=25566)
