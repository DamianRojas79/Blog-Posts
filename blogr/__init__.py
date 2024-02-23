from flask import Flask 

def create_app():
    # Crear aplicación de flask
    app= Flask (__name__)


    @app.route('/')
    def hola():
        return 'Hola Blog_Post'


    return app


