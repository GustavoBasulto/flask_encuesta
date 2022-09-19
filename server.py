from flask import Flask, render_template, request, redirect, session
import math
app = Flask(__name__)
app.secret_key = 'Geuur449' 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['nombre']=request.form['nombre']
    session['ubicacion']=request.form['ubicacion']
    session['lenguaje']=request.form['lenguaje']
    session['comentarios']=request.form['comentarios']
    return render_template("result.html", nombre=session['nombre'], ubicacion=session['ubicacion'], lenguaje=session['lenguaje'], comentarios=session['comentarios'])	 


@app.route('/result')
def result():
    return render_template("result.html", nombre=session['nombre'], ubicacion=session['ubicacion'], lenguaje=session['lenguaje'], comentarios=session['comentarios'])	 



if __name__ == "__main__":
    app.run(debug=True)