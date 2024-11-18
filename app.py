"""
Este es un módulo Flask para una aplicación web sencilla.
Contiene la configuración del servidor y las rutas básicas.
"""

from flask import *
import requests




app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/cines/<id>")
def cines(id):
    if id == None:
        response = requests.get('https://oaemdl.es/cinestar_sweb_php')
        if response.status_code == 200 :
            response = response.json()
            if response['succes']:
                return render_template('cines.html', cines = response['data'])
            else: return render_template('index.html')
    return render_template('index.html')


@app.route("/peliculas/<id>")
def peliculas(id):
    return render_template("peliculas.html")




if __name__ == "__main__":
    app.run( debug=False, port=3333 )
