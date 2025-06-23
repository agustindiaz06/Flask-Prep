from flask import Flask, url_for
import sqlite3
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


db = None


def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}


def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory


def cerrarConexion():
   global db
   db.close()
   db = None


@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
   res = cursor.fetchone()
   registros = res["cant"]
   cerrarConexion()
   return f"Hay {registros} registros en la tabla usuarios"



@app.route("/rutaNueva")
def testNueva():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT usuario , email FROM usuarios ")
   res = cursor.fetchone()
   registros = res["usuario"]
   registros2 = res["email"]
   cerrarConexion()
   return f"los usuarios que hay son los de   {registros}  en la tabla usuarios y el  email del usuario es {registros2}"