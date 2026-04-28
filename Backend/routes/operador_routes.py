from flask import Blueprint, render_template, request, redirect, url_for, session
from services.auth_service import AuthService
from repositories.solicitacao_repository import SolicitacaoRepository

operador_bp = Blueprint('operador', __name__)
auth_service = AuthService()
solicitacao_repo = SolicitacaoRepository()

@operador_bp.route('/operador/login')
def login():
    return render_template('operador/login.html')

@operador_bp.route('/operador/autenticar', methods=['POST'])
def autenticar():
    email = request.form.get('email')

    operador = auth_service.login_operador(email)

    if operador:
        session['operador_id'] = operador.id
        session['operador_nome'] = operador.nome
        return redirect(url_for('operador.dashboard'))

    return "Email não encontrado"

@operador_bp.route('/operador/dashboard')
def dashboard():
    solicitacoes = solicitacao_repo.buscar_todas()
    return render_template('operador/dashboard.html', solicitacoes=solicitacoes)

@operador_bp.route('/operador/atualizar_status/<int:id>', methods=['POST'])
def atualizar_status(id):
    status = request.form.get('status')
    solicitacao_repo.atualizar_status(id, status)
    return redirect(url_for('operador.dashboard'))