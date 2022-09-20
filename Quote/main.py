from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

def get_quote():
    url = "https://zenquotes.io/api/quotes"
    response = json.loads(requests.request("GET", url).text)
    quote = response[0]['q']
    author = response[0]['a']
    return quote,author


@app.route("/")
def index():
    quote,author = get_quote()
    return render_template("index.html",author=author, quote=quote)


app.run(host="0.0.0.0", port = 80)