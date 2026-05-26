from repositories.comentario_repository import ComentarioRepository
from models.comentario import Comentario

class ComentarioService:

    def __init__(self):
        self.comentario_repo = ComentarioRepository()

    def adicionar_comentario(self, solicitacao_id: int, usuario_id: int, tipo_autor: str, mensagem: str):
        comentario = Comentario(
            solicitacao_id=solicitacao_id,
            usuario_id=usuario_id,
            tipo_autor=tipo_autor,
            mensagem=mensagem
        )
        return self.comentario_repo.salvar(comentario)

    def listar_por_ocorrencia(self, solicitacao_id: int):
        return ComentarioRepository.listar_por_ocorrencia(solicitacao_id)
