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
    data = requests.get("https://bio.torre.co/api/bios/vimuriel")
    return render_template("profile.html", data=url)

@app.route("/perfil", methods=["POST"])
def perfil():
    name = request.form.get("name")
    url = f'https://bio.torre.co/api/bios/{name}'
    data = requests.get("https://bio.torre.co/api/bios/vimuriel")
    perfil =data.json()
    skills = perfil['strengths']
    lista = " "
    for skill in skills:
        lista = f"{lista} - {skill['name']}"

    experiences = perfil['jobs']
    education = perfil['education']

    return render_template("profile.html", data=data.json() ,skills=lista, experiences=experiences, education=education)


