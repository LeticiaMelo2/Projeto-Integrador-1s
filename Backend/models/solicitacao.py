#define p que é uma solicitação
class Solicitacao:
    def __init__(self, id=None, usuario_id=None, titulo="", descricao="", impacto="", urgencia="", prioridade="media", status="aberta", operador_id=None, criada_em=None, atualizada_em=None, fechada_em=None):
        self.id = id
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descricao = descricao
        self.impacto = impacto
        self.urgencia = urgencia
        self.prioridade = prioridade
        self.status = status
        self.operador_id = operador_id
        self.criada_em = criada_em
        self.atualizada_em = atualizada_em
        self.fechada_em = fechada_em