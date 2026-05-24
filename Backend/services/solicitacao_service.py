from repositories.solicitacao_repository import SolicitacaoRepository


class SolicitacaoService:

    def __init__(self):
        self.solicitacao_repo = SolicitacaoRepository()

    def cancelar_ocorrencia(self, ocorrencia_id: int, user_id: int):
        return self.solicitacao_repo.cancelar(
            ocorrencia_id,
            user_id
        )