from models.historico import Historico
from repositories.historico_repository import HistoricoRepository


class HistoricoService:

    @staticmethod
    def registrar(solicitacao_id, usuario_id, acao, descricao):

        historico = Historico(
            solicitacao_id=solicitacao_id,
            usuario_id=usuario_id,
            acao=acao,
            descricao=descricao
        )

        HistoricoRepository.criar(historico)