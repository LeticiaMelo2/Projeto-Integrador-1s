from ProjetoHelpDesk import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.column(database.Integer, primary_key=True)
    username = database.column(database.String, nullable=False)
    email = database.column(database.String, nullable=False, unique=True)
    senha = database.column(database.String, nullable=False)