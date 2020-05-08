from flask import Flask, render_template, request
from appi.users import User
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user", methods=["POST"])
def getUser():
    name = request.form.get("user")
    url = f'https://bio.torre.co/api/bios/{name}'
    data = requests.get(url)
    return render_template("profile.html", data=data.json())


