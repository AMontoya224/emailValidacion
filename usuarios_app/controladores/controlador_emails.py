from flask import render_template, request, redirect, session, flash
from usuarios_app import app
from usuarios_app.modelos.modelo_emails import Emails
from datetime import datetime

@app.route( '/', methods=['GET'] )
def paginaInicio():
    return render_template( "index.html")


@app.route( '/success', methods=["GET"] )
def despliegaEmail():
    if 'name' in session:
        emails = Emails.obtenerListaEmails()
        return render_template( "success.html", emails=emails )

    else:
        return redirect( '/' )


@app.route( '/decision', methods=["POST"] )
def registrarEmail():
    nuevoEmail = {
        "correo" : request.form["correo"],
        "create_at" : datetime.today()
    }
    session["correo"] = request.form["correo"]
    session["create_at"] = datetime.today()
    if not Emails.validarEmail( nuevoEmail ):
        return redirect('/')

    resultado = Emails.agregarEmail( nuevoEmail )
    if resultado == False:
        flash("Problemas con el database")
        return redirect('/')

    #emails = Emails.obtenerListaEmails()
    #for email in emails:
    #    if nuevoEmail["correo"] == email["correo"]:
    #        flash("El correo ya ha sido registrado")
    #       return redirect('/')

    return redirect( '/success' )


@app.route( '/success//<idEmail>', methods=["POST"] )
def eliminarUsuario( idEmail ):
    emailAEliminar = {
        "id": idEmail
    }
    Emails.eliminarEmail( emailAEliminar )
    return redirect( '/success' )


@app.route( '/home', methods=["POST"] )
def irHome():
    return redirect( '/' )


@app.errorhandler(404)
def paginaNoEncontrada(error):
    return "¡Lo siento! No hay respuesta. Inténtalo mas tarde"