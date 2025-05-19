from flask import Flask

app = Flask(__name__)


@app.route("/river")
def hola_river():
    return "<p>mal ahi river</p>"



@app.route("/boca")
def hola_boca():
    return "<p>aguante boca </p>"



@app.route("/SanLorenzo")
def hola_sanLorenzo():
    return "<p> san lorenzo </p>"




@app.route("/partido/<string:e1>/<string:e2>")
def partido(e1,e2):
    return f"{e1} vs {e2}"


