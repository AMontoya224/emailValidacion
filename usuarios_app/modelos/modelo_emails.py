import re
from flask import flash
from usuarios_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Emails:
    def __init__( self, id, correo, create_at ):
        self.id = id
        self.correo = correo
        self.create_at = create_at
    
    @staticmethod
    def validarEmail(nuevoEmail):
        is_valid = True
        if not EMAIL_REGEX.match(nuevoEmail["correo"]): 
            flash("Dirección de correo inválida!")
            is_valid = False
        return is_valid

    @classmethod
    def agregarEmail( cls, nuevoEmail ):
        query2 = "ALTER TABLE email AUTO_INCREMENT = 1;"
        connectToMySQL( "email_validacion" ).query_db( query2 )
        query = "INSERT INTO email(correo, create_at) VALUES(%(correo)s, %(create_at)s);"
        resultado = connectToMySQL( "email_validacion" ).query_db( query, nuevoEmail )
        return resultado
    
    @classmethod
    def obtenerListaEmails( cls ):
        query = "SELECT * FROM email;"
        resultado = connectToMySQL( "email_validacion" ).query_db( query )
        emails = []
        for email in resultado:
            emails.append( Emails( email["id"], email["correo"], email["create_at"]))
        return emails
    
    @classmethod
    def eliminarEmail( cls, emailAEliminar ):
        query = "DELETE FROM email WHERE id = %(id)s;"
        resultado = connectToMySQL( "email_validacion" ).query_db( query, emailAEliminar )
        return resultado