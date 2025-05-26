from flask import Flask, url_for

app = Flask(__name__)
@app.route("/")
def hello_wordl():
    return f""" <p>Hello, World!</p>
    <a href="{url_for('hola_river')}"> una ruta sencilla</a><br>
    <a href="{url_for('hola_boca')}"> una ruta sencilla</a><br>
    <a href="{url_for('hola_sanLorenzo')}"> una ruta sencilla</a><br>
    <a href="{url_for('partido',e1="boca",e2="river")}"> una ruta sencilla</a><br>
    
"""

@app.route("/river")
def hola_river():
    return "<p>mal ahi river</p>"


@app.route("/boca")
def hola_boca():
    return "<p>aguante boca</p>"
    


@app.route("/SanLorenzo")
def hola_sanLorenzo():
    return "<p> san lorenzo </p>"



@app.route("/partido/<string:e1>/<string:e2>")
def partido(e1,e2):
    return f"{e1} vs {e2}"


