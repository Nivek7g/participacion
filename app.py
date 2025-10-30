from flask import Flask
from config import Config
from models.database import create_tables

def create_app():
    app = Flask(__name__, template_folder='views')
    app.config.from_object(Config)

    # ------------------
    # Importar Blueprints
    # ------------------
    from controllers.auth_controller import bp as auth_controller
    app.register_blueprint(auth_controller, url_prefix='/auth')

    from controllers.dashboard_controller import bp as dashboard_controller
    app.register_blueprint(dashboard_controller)

    from controllers.estudiantes_controller import bp as estudiantes_controller
    app.register_blueprint(estudiantes_controller, url_prefix='/estudiantes')

    from controllers.cursos_controller import bp as cursos_controller
    app.register_blueprint(cursos_controller, url_prefix='/cursos')

    from controllers.inscripcion_controller import bp as inscripcion_controller
    app.register_blueprint(inscripcion_controller, url_prefix='/inscripcion')

    from controllers.usuarios_controller import bp as usuarios_controller
    app.register_blueprint(usuarios_controller, url_prefix='/usuarios')
    # ------------------

    # Inicialización de la base de datos (se hace solo en el contexto de la aplicación)
    with app.app_context():
        create_tables()

    return app

# =========================================================
# CAMBIO CLAVE para Gunicorn (Opción 1)
# =========================================================
# Creamos la instancia de la aplicación fuera del bloque __main__
# para que Gunicorn la pueda importar globalmente como 'app'.
app = create_app()

if __name__ == '__main__':
    # Este bloque solo se usa para desarrollo local (python app.py)
    app.run(host="0.0.0.0", port=5000, debug=True)