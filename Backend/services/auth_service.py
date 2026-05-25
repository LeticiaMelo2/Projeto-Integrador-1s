from repositories.operador_repository import OperadorRepository
from repositories.usuario_repository import UsuarioRepository
from werkzeug.security import generate_password_hash, check_password_hash

class AuthService: #cria uma classe chamada AuthService
    
    def __init__(self): #método que é executado automaticamente quando um objeto da classe é criado, inicializando variáveis internas
        self.operador_repo = OperadorRepository() #cria um objeto da classe OperadorRepository, que vai ser usado para acessar o bd
        self.usuario_repo = UsuarioRepository()
    
    def login_operador(self, email: str): #define o método chamado login_operador, recebendo o próprio objeto, e o email que é uma string
        operador = self.operador_repo.buscar_por_email(email) #chama a função buscar_por_email que ta no repositório, ele vai no bd e busca na tabela de operadores um com o email
                                                              #fornecido, e guarda o resultado na variável operador
        if operador: #se achar
            return operador #retorna a variável
        return None #se não, retorna none
    
    def login_usuario(self, email: str, password: str):
        usuario = self.usuario_repo.buscar_por_email(email)
        if usuario and check_password_hash(usuario.password, password):
            return usuario
        return None
    
    def cadastrar_usuario(self, first_name: str, last_name: str, email: str, password: str):
        existente = self.usuario_repo.buscar_por_email(email)
        if existente:
            return None
        
        password_hash = generate_password_hash(password)
        return self.usuario_repo.criar(first_name, last_name, email, password_hash)

    def login_usuario(self, email: str, password: str):
        usuario = self.usuario_repo.buscar_por_email(email)
        resultado = check_password_hash(usuario.password, password)
        if usuario and resultado:
            return usuario
        return None