from flask import Flask
from app.models import db, bcrypt, User
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

   
    from app.routes import main
    app.register_blueprint(main)

    return app
