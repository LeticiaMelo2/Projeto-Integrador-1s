class Usuario:
    def __init__(self, id=None, first_name="", last_name="", email="", password="", permissao_id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.permissao_id = permissao_id