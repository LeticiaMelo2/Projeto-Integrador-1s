from flask import Blueprint, render_template, request, redirect, url_for, session
from services.auth_service import AuthService
from services.estatistica_service import EstatisticaService
from repositories.solicitacao_repository import SolicitacaoRepository
from repositories.usuario_repository import UsuarioRepository
from services.comentario_service import ComentarioService
from repositories.historico_repository import HistoricoRepository

comentario_service = ComentarioService()
operador_bp = Blueprint('operador', __name__)
solicitacao_repo = SolicitacaoRepository()
estatistica_service = EstatisticaService()
usuario_repo = UsuarioRepository()
#cria todos os objetos de uma vez, pra n recriar requisição


@operador_bp.route('/operador/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST': #se for um método POST (que ta definido no html)
        ocorrencia_id = request.form.get('ocorrencia_id') #pega o id do formulário
        operador_id = session.get('operador_id') #pega id do operador logado

        solicitacao_repo.atualizar_status(ocorrencia_id, operador_id) #atualiza no bd

        return redirect(url_for('operador.dashboard')) #redireciona pro GET

    status = request.args.get('status') #pega o status
    prioridade = request.args.get('prioridade') #pega a prioridade
    usuario_id = request.args.get('usuario_id') #pega o id do usuário
#passa oq ele pegou pro repositório, atualiza lá

    resultado = solicitacao_repo.buscar_todas(status, prioridade, usuario_id)
    #busca ocorrencias com filtros escolhidos
    total_por_status = estatistica_service.total_por_status()
    total_por_prioridade = estatistica_service.total_por_prioridade()
    #busca numeros pros contadores do dashboard
    usuarios = usuario_repo.buscar_todos()
    #busca todos os usuários p colocar no dropdown de filtros no HTML

    return render_template('operador/dashboard.html',
                           dados=resultado,
                           total_por_status=total_por_status,
                           total_por_prioridade=total_por_prioridade,
                           usuarios=usuarios,
                           status=status,
                           prioridade=prioridade,
                           usuario_id=usuario_id)

    #o html usa essas variáveis, e passa status, prioridade e usuario_id por conta dos filtros

@operador_bp.route('/operador/fechar/<int:id>', methods=['POST'])
def fechar(id):
    sucesso, mensagem = solicitacao_repo.fechar(id)
    #repositorio fechar retorna uma tupla com valores, que retorna True ou False euma mensagem
    #nessa linha a tupla é desempacotada

    if not sucesso:
        return mensagem

    return redirect(url_for('operador.dashboard'))

@operador_bp.route('/operador/historico/<int:solicitacao_id>', methods=['GET', 'POST'])
def historico(solicitacao_id):
    if 'operador_id' not in session:
        return redirect(url_for('usuario.login')) #proteção de rota, verificação de autenticação

    if request.method == 'POST':
        mensagem = request.form.get('mensagem', '').strip()
        #('mensagem', ''), o segundo espaço é o padrão, caso n tenha mensagem pra n trabalhar com None sem querer
        #e 'mensagem' vem do HTML (name do campo)
        #strip() apaga espaços antes e dps da string
        if mensagem:
            comentario_service.adicionar_comentario(
                solicitacao_id,
                session.get('operador_id'),
                'operador',
                mensagem
            )
        return redirect(url_for('operador.historico', solicitacao_id=solicitacao_id))

    historico = HistoricoRepository.listar_por_solicitacao(solicitacao_id)
    comentarios = comentario_service.listar_por_ocorrencia(solicitacao_id)

    return render_template(
        'operador/historico.html',
        historico=historico,
        comentarios=comentarios,
        solicitacao_id=solicitacao_id
    )