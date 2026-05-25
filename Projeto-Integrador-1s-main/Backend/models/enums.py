from enum import Enum

class StatusSolicitacao(Enum):
    ABERTO = "ABERTO"
    EM_ANDAMENTO = "EM_ANDAMENTO"
    FINALIZADO = "FINALIZADO"
    CANCELADO = "CANCELADO"