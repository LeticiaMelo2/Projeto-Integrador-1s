from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config[SQLALCHEMY_DATABASE_URI] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "893ccf2276e398115a8f7e5574f9e8a4"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"


from HelpDesk import routes
