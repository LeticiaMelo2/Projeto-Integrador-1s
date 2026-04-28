from ProjetoHelpDesk import database, app 
from .models import Usuario

with app.context():
    database.create_all()