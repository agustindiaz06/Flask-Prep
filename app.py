from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/river")
def hola_river():
    return "<p>mal ahi river</p>"



@app.route("/boca")
def hola_boca():
    return "<p>aguante boca </p>"



@app.route("/SanLorenzo")
def hola_sanLorenzo():
    return "<p> san lorenzo </p>"
