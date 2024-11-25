from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('app.config.Config')

    # Register blueprints (routes)
    from app.routes import main
    app.register_blueprint(main)

    return app