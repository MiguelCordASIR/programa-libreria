from flask import Flask,render_template,abort
app= Flask(__name__)
import os

import json
with open("books.json") as fichero:
    datos=json.load(fichero)

@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("inicio.html",datos=datos)

@app.route('/libro/<isbn>')
def libro(isbn):
    for libro in datos:
        try:
            if libro["isbn"] == isbn:
                return render_template("libro.html",dato=libro)
        except:
            return "Error 404"
@app.route('/categoria/<categoria>')
def categoria(categoria):
        return render_template("categoria.html",dato=datos,categoria=categoria)
    
port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)