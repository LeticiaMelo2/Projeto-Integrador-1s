from datetime import datetime

class Historico:
    def __init__(
        self,
        id=None,
        solicitacao_id=None,
        usuario_id=None,
        acao="",
        descricao="",
        data=None
    ):
        self.id = id
        self.solicitacao_id = solicitacao_id
        self.usuario_id = usuario_id
        self.acao = acao
        self.descricao = descricao
        self.data = data or datetime.now()