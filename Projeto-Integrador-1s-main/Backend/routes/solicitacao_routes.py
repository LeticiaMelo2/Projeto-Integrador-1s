from flask import Blueprint, jsonify, request
from services.solicitacao_service import SolicitacaoService

solicitacao_bp = Blueprint('solicitacao', __name__)

service = SolicitacaoService()


@solicitacao_bp.route('/ocorrencias/<int:ocorrencia_id>/cancelar', methods=['PUT'])
def cancelar_ocorrencia(ocorrencia_id):
    dados = request.get_json()

    user_id = dados.get('user_id')

    sucesso, mensagem = service.cancelar_ocorrencia(
        ocorrencia_id,
        user_id
    )

    if sucesso:
        return jsonify({
            'success': True,
            'message': mensagem
        }), 200

    return jsonify({
        'success': False,
        'message': mensagem
    }), 400