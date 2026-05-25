from services.historico_service import HistoricoService


HistoricoService.registrar(
    solicitacao_id=nova_solicitacao.id,
    usuario_id=usuario.id,
    acao="CRIACAO",
    descricao="Solicitação criada pelo usuário"
)


HistoricoService.registrar(
    solicitacao_id=solicitacao.id,
    usuario_id=operador.id,
    acao="ALTERACAO_STATUS",
    descricao=f"Status alterado para {novo_status}"
)


HistoricoService.registrar(
    solicitacao_id=solicitacao.id,
    usuario_id=operador.id,
    acao="FINALIZACAO",
    descricao="Solicitação finalizada"
)