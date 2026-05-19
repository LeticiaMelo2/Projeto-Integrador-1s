"""define o que é um operador, criadno uma formula, todo operador tem id, nome e email"""

class Operador:
    def __init__(self, id=None, nome="", email=""):
        self.id = id
        self.nome = nome
        self.email = email

'''o self serve para as variáveis não serem locais, sem ele elas seriam locais e sumiriam quando o __init__ acabasse, é uma forma de mostrar 
para o python que esse método/função pertence ao objeto, e não é uma função solta'''