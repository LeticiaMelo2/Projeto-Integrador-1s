"""define o que é um operador, criadno uma formula, todo operador tem id, nome e email, no caso"""

class Operador:
    def __init__(self, id=None, nome="", email=""):
        self.id = id
        self.nome = nome
        self.email = email