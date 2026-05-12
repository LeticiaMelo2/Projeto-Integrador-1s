from flask import Blueprint, render_template, request, redirect, url_for, session
from services.auth_service import AuthService
from services.estatistica_service import EstatisticaService
from repositories.solicitacao_repository import SolicitacaoRepository
from repositories.usuario_repository import UsuarioRepository

operador_bp = Blueprint('operador', __name__)
auth_service = AuthService()
solicitacao_repo = SolicitacaoRepository()
estatistica_service = EstatisticaService()
usuario_repo = UsuarioRepository()

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

@operador_bp.route('/operador/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        ocorrencia_id = request.form.get('ocorrencia_id')
        operador_id = session.get('operador_id')

        solicitacao_repo.atualizar_status(ocorrencia_id, operador_id)

        return redirect(url_for('operador.dashboard'))

    status = request.args.get('status')
    prioridade = request.args.get('prioridade')
    usuario_id = request.args.get('usuario_id')

    resultado = solicitacao_repo.buscar_todas(status, prioridade, usuario_id)
    total_por_status = estatistica_service.total_por_status()
    total_por_prioridade = estatistica_service.total_por_prioridade()
    usuarios = usuario_repo.buscar_todos()

    return render_template('operador/dashboard.html',
                           dados=resultado,
                           total_por_status=total_por_status,
                           total_por_prioridade=total_por_prioridade,
                           usuarios=usuarios,
                           status=status,
                           prioridade=prioridade,
                           usuario_id=usuario_id)

@operador_bp.route('/operador/fechar/<int:id>', methods=['POST'])
def fechar(id):
    sucesso, mensagem = solicitacao_repo.fechar(id)

    if not sucesso:
        return mensagem

    return redirect(url_for('operador.dashboard'))