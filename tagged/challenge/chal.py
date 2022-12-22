from flask import Flask, request, redirect
from bs4 import BeautifulSoup
import secrets

app = Flask(__name__)
pages = {}
SAFE_TAGS = ['i', 'b', 'p', 'br']

with open("home.html") as home:
    HOME_PAGE = home.read()

@app.route("/")
def home():
    return HOME_PAGE

@app.route("/add", methods=['POST'])
def add():
    contents = request.form.get('contents')
    
    tree = BeautifulSoup(contents)
    for element in tree.find_all():
        if element.name not in SAFE_TAGS or len(element.attrs) > 0:
            return "This HTML looks sus."

    new_id = secrets.token_hex(16)
    pages[new_id] = str(tree)
    print(pages[new_id])
    return redirect("/page?id=" + new_id)

@app.route("/page")
def page():
    key = request.args.get('id')
    if key is None or key not in pages:
        return "Nothing here!\n"
    return f"<!DOCTYPE html><html><body>{pages[key]}</body></html>"

