from flask import Flask, url_for, render_template
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



@app.route("/usuarios")
def testNueva():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT usuario ,id FROM usuarios ")
   listaUsuarios = cursor.fetchall()
   cerrarConexion()
   return render_template("usuarios.html", usuarios=listaUsuarios)

# modificar la ruta para que acepte el id como parametro LISTO

# modificar la consulta de sql para que solamente seleccione el que tiene ese id (usar un ? donde va el valor)

# cambiar fetchall por fetchone LISTO

# cambiar la plantilla por detalleUsuario  LISTO

# pasarle ese resultado a la plantilla como usr (que ya no es una lista sino un solo usuario) LISTO
@app.route("/usuario/<int:id>")
def detalle(id):
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT usuario, telefono , direccion , email  FROM usuarios WHERE id = ?", (id,))
   Usuario = cursor.fetchone()
   cerrarConexion()
   return render_template("detalleUsuario.html", usr=Usuario)