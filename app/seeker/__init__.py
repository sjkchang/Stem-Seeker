"""
__init__.py
====================================
The core module of my project
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(testing):
    """
    Initializes flask app
    Parameters
    ----------
    testing
        boolean to determine if the app is actually being deployed or if it is running a test
    """
    app = Flask(__name__, instance_relative_config=False, template_folder='templates')

    if not testing:
        # load the instance config, if it exists, when not testing
        app.config.from_object('config.Config')
    else:
        app.config.from_object('config.TestConfig')

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Include our routes
        from .routes import home, internship, userManagement
        from .models.Internship import Internship
        #db.drop_all()
        #db.create_all()

        return app
