
from flask import render_template, request, redirect, url_for,Flask,jsonify,make_response, session
from src import app
from src.models.usuarios import UsuariosModel
from random import choice
from urllib.request import urlopen
import webbrowser
import hashlib

app.secret_key ="hola"

@app.route('/usuarios/', methods =['GET', 'POST'])
def elegir_opcion():
   
    if request.method == 'GET':
      
        return render_template('/usuarios/inicio.html')

@app.route('/usuarios/ingreso_usuarios', methods =['GET', 'POST'])
def ingreso_usuarios():

    if request.method == 'GET':
        return render_template('/usuarios/ingreso.html')
    else:
        correo = request.form.get('correo')
        clave = request.form.get('clave')
        encriptado = hashlib.md5(clave.encode())
        claveEncriptada = encriptado.hexdigest()
        usuariosModel = UsuariosModel()
        id_usuario = usuariosModel.ingreso_usuarios(correo, claveEncriptada)

        user = id_usuario
        session["user"] = user
        if user == "":
            return redirect(url_for("ingreso_usuarios"))
        else:
            return redirect(url_for("elegir_opcion_link"))

@app.route('/usuarios/elegir_opcion_link', methods =['GET', 'POST'])
def elegir_opcion_link():

    if "user" in session:
        user = session["user"]
        if request.method == 'GET': 
            return render_template('/usuarios/gestion_link.html', user = user)
    else:
        return redirect(url_for("ingreso_usuarios"))

@app.route('/usuarios/ver_links', methods =['GET', 'POST'])
def ver_links():

    if "user" in session:
        user = session["user"]

        if request.method == 'GET':

            usuariosModel =UsuariosModel()

            enlaces = usuariosModel.ver_links(int(user))
   
            return render_template('usuarios/ver_links.html', enlaces = enlaces)
    else:
        return redirect(url_for("ingreso_usuarios"))

@app.route('/usuarios/link', methods =['GET', 'POST'])
def insertar_link():
    if "user" in session:
        user = session["user"]

        if request.method == 'GET':
            return render_template('/usuarios/link.html')
        else:
            nombre = request.form.get('link')
            longitud = 4
            valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            p = ""
            p = p.join([choice(valores) for i in range(longitud)])
            usuariosModel = UsuariosModel()
            usuariosModel.insertar_link(nombre,p,int(user))
            return redirect(url_for("ver_links"))
    else:
        return redirect(url_for("ingreso_usuarios"))

@app.route('/<random>', methods = ['GET'])
def consultando_link(random):

  
    miLink = UsuariosModel()
    enlaceLimpio = miLink.consultar_link(random)

    webbrowser.open(enlaceLimpio)

    return ("La pagina se abrira en otra pestaña")
    

@app.route('/usuarios/registro_usuarios', methods =['GET', 'POST'])
def registro_usuarios():
   
    if request.method == 'GET':
      
        return render_template('/usuarios/registro.html')
    else:

        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        clave = request.form.get('clave')
        encriptado = hashlib.md5(clave.encode())
        claveEncriptada = encriptado.hexdigest()
        usuariosModel = UsuariosModel()
        usuariosModel.registrar_usuario(nombre,correo,claveEncriptada)
        
        return redirect(url_for('elegir_opcion'))

@app.route('/usuarios/eliminar_link', methods =['POST', 'GET'])
def eliminar_link():
    if "user" in session:
        user = session["user"]
        if request.method == 'GET': 
            return render_template('/usuarios/ver_links.html')
        else:
            codigo = request.form.get('codigo')
            usuariosModel = UsuariosModel()
            usuariosModel.eliminar_link(codigo)
            return redirect(url_for("ver_links"))

@app.route('/usuarios/actualizar_link', methods =['PUT', 'GET'])
def actualizar_link():
    if "user" in session:
        user = session["user"]

        if request.method == 'GET': 
            return render_template('/usuarios/actualizar_links.html')

        else:
            codigo = request.form.get('codigo')
            nuevo_enlace = request.form.get('nuevo_enlace')
            usuariosModel = UsuariosModel()
            usuariosModel.actualizar_link(nuevo_enlace, codigo)
            return redirect(url_for("ver_links"))
