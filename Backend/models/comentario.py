from datetime import datetime

class Comentario:
    def __init__(
        self,
        id=None,
        solicitacao_id=None,
        usuario_id=None,
        tipo_autor="usuario",
        mensagem="",
        criado_em=None
    ):
        self.id = id
        self.solicitacao_id = solicitacao_id
        self.usuario_id = usuario_id
        self.tipo_autor = tipo_autor
        self.mensagem = mensagem
        self.criado_em = criado_em or datetime.now()
