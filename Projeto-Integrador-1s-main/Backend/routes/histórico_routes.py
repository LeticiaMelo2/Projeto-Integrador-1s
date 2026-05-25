from flask import Blueprint, jsonify
from repositories.historico_repository import HistoricoRepository

historico_bp = Blueprint('historico', __name__)


@historico_bp.route('/historico/<int:solicitacao_id>', methods=['GET'])
def listar_historico(solicitacao_id):

    historico = HistoricoRepository.listar_por_solicitacao(solicitacao_id)

    return jsonify(historico)