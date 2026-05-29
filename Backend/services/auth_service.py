from repositories.usuario_repository import UsuarioRepository
from werkzeug.security import generate_password_hash, check_password_hash


class AuthService:  # cria uma classe chamada AuthService

    def __init__(
            self):  # método que é executado automaticamente quando um objeto da classe é criado, inicializando variáveis internas
        self.usuario_repo = UsuarioRepository()

    def login_usuario(self, email: str, password: str):
        usuario = self.usuario_repo.buscar_por_email(email)
        if not usuario:
            return None
        if check_password_hash(usuario.password, password):
            return usuario
        return None

    def cadastrar_usuario(self, first_name: str, last_name: str, email: str, password: str):
        existente = self.usuario_repo.buscar_por_email(email)
        if existente:
            return None

        password_hash = generate_password_hash(password)
        return self.usuario_repo.criar(first_name, last_name, email, password_hash)