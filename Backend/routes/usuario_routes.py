from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services.auth_service import AuthService
from services.classificacao_service import calcular_prioridade
from services.solicitacao_service import SolicitacaoService
from services.comentario_service import ComentarioService
from repositories.solicitacao_repository import SolicitacaoRepository
from repositories.historico_repository import HistoricoRepository
from forms.usuario_forms import RegisterForm

usuario_bp = Blueprint('usuario', __name__)
auth_service = AuthService()
solicitacao_repo = SolicitacaoRepository()
comentario_service = ComentarioService()


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
            return render_template('usuario/login_confirmacao.html', name=usuario.first_name)

        elif usuario.permissao_id == 2:
            return redirect(url_for('operador.dashboard'))

    return render_template('usuario/login_error.html')


@usuario_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        resultado = auth_service.cadastrar_usuario(
            form.first_name.data,
            form.last_name.data,
            form.email.data,
            form.password.data,
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


@usuario_bp.route('/cancelar_ocorrencia/<int:solicitacao_id>', methods=['POST'])
def cancelar_ocorrencia(solicitacao_id):
    if 'user_id' not in session:
        flash('Usuário não autenticado')
        return redirect(url_for('usuario.login'))

    usuario_id = session['user_id']
    service = SolicitacaoService()

    sucesso, mensagem = service.cancelar_ocorrencia(
        solicitacao_id,
        usuario_id
    )

    flash(mensagem)
    return redirect(url_for('usuario.ocorrencias'))


@usuario_bp.route('/historico/<int:solicitacao_id>', methods=['GET', 'POST'])
def historico(solicitacao_id):
    if 'user_id' not in session and 'operador_id' not in session:
        flash('Autenticação necessária')
        return redirect(url_for('usuario.login'))

    if request.method == 'POST':
        mensagem = request.form.get('mensagem', '').strip()
        if mensagem:
            autor_id = session.get('user_id') or session.get('operador_id')
            tipo_autor = 'usuario' if session.get('user_id') else 'operador'
            comentario_service.adicionar_comentario(
                solicitacao_id,
                autor_id,
                tipo_autor,
                mensagem
            )
        return redirect(url_for('usuario.historico', solicitacao_id=solicitacao_id))

    historico = HistoricoRepository.listar_por_solicitacao(solicitacao_id)
    comentarios = comentario_service.listar_por_ocorrencia(solicitacao_id)

    return render_template(
        'usuario/historico.html',
        historico=historico,
        comentarios=comentarios,
        solicitacao_id=solicitacao_id
    )