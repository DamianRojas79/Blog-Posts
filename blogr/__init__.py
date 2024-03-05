from flask import Flask 

def create_app():
    # Crear aplicación de flask
    app= Flask (__name__)

    # Aplica configuracion del sistema del archivo config
    app.config.from_object('config.Config')

    # Registrar Vistas
    from blogr import home
    app.register_blueprint(home.bp)

    from blogr import auth
    app.register_blueprint(auth.bp)
   
    from blogr import post
    app.register_blueprint(post.bp)


    return app


