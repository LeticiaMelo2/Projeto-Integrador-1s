from flask import Blueprint, render_template, request, redirect, url_for, session
from services.auth_service import AuthService
from services.classificacao_service import calcular_prioridade
from repositories.solicitacao_repository import SolicitacaoRepository
from forms.usuario_forms import RegisterForm

usuario_bp = Blueprint('usuario', __name__)
auth_service = AuthService()
solicitacao_repo = SolicitacaoRepository()

@usuario_bp.route('/')
def login():
    return render_template('usuario/login.html')

@usuario_bp.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form.get('email')
    password = request.form.get('password')

    usuario = auth_service.login_usuario(email, password)

    if usuario:
        session['user_id'] = usuario.id
        session['user_name'] = usuario.first_name
        session['permissao'] = usuario.permissao_id

        if usuario.permissao_id == 1:
            return redirect(url_for('usuario.home'))

        elif usuario.permissao_id == 2:
            return redirect(url_for('operador.dashboard'))

    return "Email ou senha incorretos"

@usuario_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        resultado = auth_service.cadastrar_usuario(
            form.first_name.data,
            form.last_name.data,
            form.email.data,
            form.password.data
        )

        if not resultado:
            return "Email já cadastrado"

        return redirect('/')

    return render_template('usuario/register.html', form=form)

@usuario_bp.route('/home')
def home():
    name = session.get('user_name')
    return render_template('usuario/home.html', name=name)

@usuario_bp.route('/criar_ocorrencia', methods=['POST'])
def criar_ocorrencia():
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    impacto = request.form.get('impacto')
    urgencia = request.form.get('urgencia')

    prioridade = calcular_prioridade(impacto, urgencia)
    user_id = session.get('user_id')
    status_id = 1

    solicitacao_repo.criar(user_id, titulo, descricao, impacto, urgencia, prioridade, status_id)

    return redirect(url_for('usuario.sucesso'))

@usuario_bp.route('/ticket')
def ticket():
    return render_template('usuario/ticket.html')

@usuario_bp.route('/sucesso')
def sucesso():
    return render_template('usuario/sucesso.html')

@usuario_bp.route('/ocorrencias')
def ocorrencias():
    filtro = request.args.get('filtro', 'todos')
    user_id = session.get('user_id')

    dados = solicitacao_repo.buscar_por_usuario(user_id, filtro)

    return render_template('usuario/status.html', dados=dados, filtro=filtro)