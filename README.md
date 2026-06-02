
<div align="center">
    <h1>Sistema de Controle de Solicitações Corporativas (SCSC)</h1>
</div>

---

<h2 id="desc"> 📖 Descrição Geral</h2>
# 🎫 Sistema de Controle de Solicitações Corporativas (SCSC)

O SCSC é uma plataforma web desenvolvida para digitalizar e organizar o gerenciamento de solicitações internas em ambiente corporativo. O sistema permite que colaboradores registrem solicitações, acompanhem seu andamento e que operadores gerenciem e atualizem o status dessas demandas, substituindo métodos informais como e-mails e anotações descentralizadas.

---

## 📋 Funcionalidades

### 🔹 Usuário
- Cadastro e login com autenticação por e-mail e senha, com redirecionamento automático conforme o perfil
- Abertura de solicitações informando título, descrição, impacto e urgência
- Classificação automática de prioridade (Baixa, Média ou Alta) com base nos fatores informados
- Acompanhamento das solicitações com filtro por status (aberta, em andamento, finalizada, cancelada)
- Cancelamento de solicitações abertas pelo próprio usuário
- Visualização do histórico e comentários de cada solicitação

### 🔹 Operador
- Login dedicado via painel administrativo
- Dashboard com visão geral de todas as solicitações
- Filtros por status, prioridade e usuário
- Atualização de status (Aberta → Em andamento → Finalizada)
- Estatísticas com total de solicitações por status e por prioridade
- Canal de comunicação com usuários via comentários

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Descrição |
|-----------|-----------|-----------|
| Linguagem Backend | Python 3.10+ | Linguagem principal para desenvolvimento do back-end |
| Framework Backend | Flask | Framework minimalista para criação de aplicações web em Python |
| Linguagem Frontend | JavaScript | Linguagem para adicionar interatividade ao frontend |
| Linguagem de Estilo | CSS | Definição de estilos e layouts das páginas web |
| Linguagem de Estrutura | HTML5 | Estruturação do conteúdo das páginas web |
| Banco de Dados | MySQL 8.x | Sistema de gerenciamento de banco de dados relacional |
| Autenticação | Flask Session + Werkzeug | Controle de sessão e hash de senhas |
| Formulários | Flask-WTF + WTForms | Validação e criação de formulários |
| Conexão com BD | mysql-connector-python | Conexão entre Python e MySQL |
| Controle de Versão | Git e GitHub | Sistema de controle de versão distribuído |
| IDE | PyCharm / VS Code | IDEs utilizadas para o desenvolvimento |

---

## 📐 Arquitetura do Projeto

O projeto adota uma **arquitetura em camadas**, separando as responsabilidades em módulos bem definidos:

| Camada | Responsabilidade |
|--------|-----------------|
| **Models** | Representam as entidades do sistema (Usuario, Solicitacao, Historico, Comentario) |
| **Repositories** | Acesso ao banco de dados via queries SQL puras |
| **Services** | Regras de negócio (prioridade, autenticação, estatísticas) |
| **Routes** | Endpoints Flask que recebem requisições e retornam respostas |

### 🔄 Fluxo de Operação

```
Usuário (HTML/CSS/JS)
        ↓
  Route (Flask)
        ↓
  Service (regra de negócio)
        ↓
  Repository (query SQL)
        ↓
  Banco de Dados (MySQL)
```

**Benefícios da arquitetura:** separação de responsabilidades, fácil manutenção e escalabilidade para novas funcionalidades.

---

## 📁 Estrutura do Projeto

```
Projeto-Integrador-1s/
├── Backend/
│   ├── main.py                        # Ponto de entrada da aplicação
│   ├── config.py                      # Configurações do banco de dados
│   ├── .env                           # Variáveis de ambiente
│   ├── .env.example                   # Exemplo de variáveis de ambiente
│   ├── requirements.txt               # Dependências do projeto
│   ├── database/
│   │   └── connection.py              # Conexão com o MySQL (padrão Singleton)
│   ├── models/
│   │   ├── comentario.py
│   │   ├── historico.py
│   │   ├── solicitacao.py
│   │   └── usuario.py
│   ├── repositories/
│   │   ├── comentario_repository.py
│   │   ├── historico_repository.py
│   │   ├── solicitacao_repository.py
│   │   └── usuario_repository.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── classificacao_service.py
│   │   ├── comentario_service.py
│   │   ├── estatistica_service.py
│   │   ├── historico_service.py
│   │   └── solicitacao_service.py
│   ├── routes/
│   │   ├── historico_routes.py
│   │   ├── operador_routes.py
│   │   └── usuario_routes.py
│   └── forms/
│       └── usuario_forms.py
└── Frontend/
    ├── static/
    │   ├── css/
    │   │   └── styles.css
    │   ├── images/
    │   └── js/
    └── templates/
        ├── operador/
        │   ├── dashboard.html
        │   └── historico.html
        └── usuario/
            ├── historico.html
            ├── home.html
            ├── login.html
            ├── login_confirmacao.html
            ├── login_error.html
            ├── register.html
            ├── status.html
            ├── sucesso.html
            └── ticket.html
```

---

## 🗄️ Banco de Dados

### Diagrama de Relacionamento

<img width="832" height="569" alt="image" src="https://github.com/user-attachments/assets/2bdc2e19-bd6c-4657-bcd9-9b407d8074a9" />

O banco de dados é composto por **6 tabelas** com os seguintes relacionamentos:

| Tabela | Descrição |
|--------|-----------|
| `usuarios` | Armazena os dados dos usuários e operadores do sistema |
| `permissao` | Define o tipo de acesso: `usuario` (1) ou `operador` (2) |
| `ocorrencias` | Tabela central com todas as solicitações abertas no sistema |
| `status` | Possíveis estados: `aberta`, `em andamento`, `finalizada`, `cancelada` |
| `comentarios` | Comentários feitos por usuários ou operadores em uma solicitação |
| `historico` | Registro de todas as ações realizadas em uma solicitação |

### Script de Criação

Para recriar o banco de dados, crie um banco com o nome `dbprojetointegrador1` no MySQL Workbench e execute o script abaixo:

```sql
-- Tabela de permissões
CREATE TABLE `permissao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `permissao` VALUES (1,'usuario'),(2,'operador');

-- Tabela de status
CREATE TABLE `status` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `status` VALUES (1,'aberta'),(2,'em andamento'),(3,'finalizada'),(4,'cancelada');

-- Tabela de usuários
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(300) NOT NULL,
  `last_name` varchar(300) NOT NULL,
  `email` varchar(300) NOT NULL,
  `password` varchar(350) NOT NULL,
  `permissao_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  CONSTRAINT `fk_permissao` FOREIGN KEY (`permissao_id`) REFERENCES `permissao` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabela de ocorrências
CREATE TABLE `ocorrencias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(200) DEFAULT NULL,
  `descricao` text,
  `impacto` varchar(20) DEFAULT NULL,
  `urgencia` varchar(20) DEFAULT NULL,
  `prioridade` varchar(20) DEFAULT NULL,
  `dataHora` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `operador_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_status` FOREIGN KEY (`status_id`) REFERENCES `status` (`id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `fk_ocorrencias_operador` FOREIGN KEY (`operador_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabela de comentários
CREATE TABLE `comentarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `solicitacao_id` int NOT NULL,
  `usuario_id` int NOT NULL,
  `tipo_autor` varchar(20) NOT NULL,
  `mensagem` text NOT NULL,
  `criado_em` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_comentarios_ocorrencia` FOREIGN KEY (`solicitacao_id`) REFERENCES `ocorrencias` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabela de histórico
CREATE TABLE `historico` (
  `id` int NOT NULL AUTO_INCREMENT,
  `solicitacao_id` int NOT NULL,
  `usuario_id` int NOT NULL,
  `acao` varchar(100) DEFAULT NULL,
  `descricao` text,
  `data` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_historico_ocorrencia` FOREIGN KEY (`solicitacao_id`) REFERENCES `ocorrencias` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

---

## ⚙️ Como Executar

### Pré-requisitos

- Python 3.10 ou superior
- MySQL 8.x instalado e rodando
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/LeticiaMelo2/Projeto-Integrador-1s.git
cd Projeto-Integrador-1s
```

### 2. Crie e ative o ambiente virtual

```bash
cd Backend
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` dentro da pasta `Backend/` com base no `.env.example`:

```env
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=dbprojetointegrador1
```

### 5. Crie o banco de dados

Abra o MySQL Workbench e execute o script SQL da seção acima.

### 6. Execute o sistema

```bash
python main.py
```

Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Funcionalidades em Detalhe

---

### 1. Cadastro de Usuário

O usuário acessa `/register`, preenche nome, e-mail e senha. O sistema verifica se o e-mail já existe e, caso contrário, salva a senha com hash de segurança.

```python
# services/auth_service.py
def cadastrar_usuario(self, first_name, last_name, email, password):
    existente = self.usuario_repo.buscar_por_email(email)
    if existente:
        return None  # e-mail já cadastrado

    password_hash = generate_password_hash(password)
    return self.usuario_repo.criar(first_name, last_name, email, password_hash)
```

---

### 2. Login do Usuário

O usuário informa e-mail e senha. O sistema busca o cadastro no banco e valida a senha com `check_password_hash`. Se válido, salva os dados na sessão e redireciona conforme a permissão.

```python
# services/auth_service.py
def login_usuario(self, email, password):
    usuario = self.usuario_repo.buscar_por_email(email)
    if usuario and check_password_hash(usuario.password, password):
        return usuario
    return None

# routes/usuario_routes.py
def autenticar():
    usuario = auth_service.login_usuario(email, password)
    if usuario:
        session['user_id']   = usuario.id
        session['user_name'] = usuario.first_name
        session['permissao'] = usuario.permissao_id

        if usuario.permissao_id == 1:
            return render_template('usuario/login_confirmacao.html')
        elif usuario.permissao_id == 2:
            return redirect(url_for('operador.dashboard'))
```

---

### 3. Login do Operador

O operador acessa `/operador/login` e informa apenas o e-mail. O sistema busca o cadastro na tabela de operadores e, se encontrado, inicia a sessão de operador.

```python
# services/auth_service.py
def login_operador(self, email):
    operador = self.operador_repo.buscar_por_email(email)
    if operador:
        return operador
    return None
```

---

### 4. Abertura de Solicitação

O usuário preenche título, descrição, impacto e urgência. O backend calcula a prioridade automaticamente e salva a solicitação com status inicial **"aberta"**.

```python
# routes/usuario_routes.py
def criar_ocorrencia():
    titulo    = request.form.get('titulo')
    descricao = request.form.get('descricao')
    impacto   = request.form.get('impacto')   # "Alta", "Média" ou "Baixa"
    urgencia  = request.form.get('urgencia')

    prioridade = calcular_prioridade(impacto, urgencia)
    user_id    = session.get('user_id')

    solicitacao_repo.criar(user_id, titulo, descricao, impacto, urgencia, prioridade, status_id=1)
    return redirect(url_for('usuario.sucesso'))
```

```python
# services/classificacao_service.py
def calcular_prioridade(impacto, urgencia):
    tabela = {"Alta": 3, "Média": 2, "Baixa": 1}
    soma = tabela.get(impacto, 1) + tabela.get(urgencia, 1)

    if soma >= 5: return "Alta"
    elif soma == 4: return "Média"
    else: return "Baixa"
```

> **Exemplo:** impacto `Alta` (3) + urgência `Média` (2) = soma `5` → prioridade **Alta**

---

### 5. Acompanhamento de Solicitações

O usuário acessa `/ocorrencias` e pode filtrar suas solicitações por status. O sistema busca apenas as ocorrências do usuário logado.

```python
# routes/usuario_routes.py
def ocorrencias():
    filtro  = request.args.get('filtro', 'todos')
    user_id = session.get('user_id')
    dados   = solicitacao_repo.buscar_por_usuario(user_id, filtro)
    return render_template('usuario/status.html', dados=dados, filtro=filtro)
```

---

### 6. Cancelamento de Solicitação

O usuário pode cancelar uma solicitação que ainda está aberta. O sistema valida se o chamado pertence ao usuário antes de cancelar.

```python
# routes/usuario_routes.py
def cancelar_ocorrencia(solicitacao_id):
    usuario_id = session['user_id']
    service    = SolicitacaoService()
    sucesso, mensagem = service.cancelar_ocorrencia(solicitacao_id, usuario_id)
    flash(mensagem)
    return redirect(url_for('usuario.ocorrencias'))
```

---

### 7. Comentários na Solicitação

Tanto o usuário quanto o operador podem adicionar comentários em uma solicitação. O sistema identifica o tipo de autor (`usuario` ou `operador`) e registra a mensagem com data e hora.

```python
# services/comentario_service.py
def adicionar_comentario(self, solicitacao_id, usuario_id, tipo_autor, mensagem):
    comentario = Comentario(
        solicitacao_id=solicitacao_id,
        usuario_id=usuario_id,
        tipo_autor=tipo_autor,  # "usuario" ou "operador"
        mensagem=mensagem
    )
    return self.comentario_repo.salvar(comentario)
```

---

### 8. Dashboard do Operador

O operador visualiza todas as solicitações com filtros por status, prioridade e usuário. O dashboard também exibe estatísticas gerais do sistema.

```python
# routes/operador_routes.py
def dashboard():
    status     = request.args.get('status')
    prioridade = request.args.get('prioridade')
    usuario_id = request.args.get('usuario_id')

    resultado            = solicitacao_repo.buscar_todas(status, prioridade, usuario_id)
    total_por_status     = estatistica_service.total_por_status()
    total_por_prioridade = estatistica_service.total_por_prioridade()

    return render_template('operador/dashboard.html',
                           dados=resultado,
                           total_por_status=total_por_status,
                           total_por_prioridade=total_por_prioridade)
```

---

### 9. Fechamento de Solicitação

O operador pode fechar uma solicitação pelo dashboard. O sistema registra o fechamento e atualiza o status no banco de dados.

```python
# routes/operador_routes.py
@operador_bp.route('/operador/fechar/<int:id>', methods=['POST'])
def fechar(id):
    sucesso, mensagem = solicitacao_repo.fechar(id)
    if not sucesso:
        return mensagem
    return redirect(url_for('operador.dashboard'))
```

---

### 10. Histórico da Solicitação

Usuários e operadores podem acessar o histórico completo de uma solicitação, visualizando todas as mudanças de status e comentários registrados.

```python
# routes/usuario_routes.py
def historico(solicitacao_id):
    historico   = HistoricoRepository.listar_por_solicitacao(solicitacao_id)
    comentarios = comentario_service.listar_por_ocorrencia(solicitacao_id)
    return render_template('usuario/historico.html',
                           historico=historico,
                           comentarios=comentarios)
```

---

## 🔐 Perfis de Acesso

| Perfil | Rota de Login | Permissões |
|--------|--------------|------------|
| Usuário | `/` | Abrir e acompanhar solicitações |
| Operador | `/operador/login` | Gerenciar todas as solicitações |

---

## ⚖️ Regra de Classificação de Prioridade

A prioridade é calculada automaticamente com base nos fatores **Impacto** e **Urgência** informados pelo usuário na abertura da solicitação:

| Impacto | Urgência | Prioridade |
|---------|----------|-----------|
| Alta | Alta | 🔴 Alta |
| Alta | Média | 🔴 Alta |
| Média | Alta | 🔴 Alta |
| Alta | Baixa | 🟡 Média |
| Média | Média | 🟡 Média |
| Baixa | Alta | 🟡 Média |
| Média | Baixa | 🟢 Baixa |
| Baixa | Média | 🟢 Baixa |
| Baixa | Baixa | 🟢 Baixa |

---

<h2 id="colab"> 🤝 Colaboradores</h2>

Um agradecimento especial a todas as pessoas que contribuíram para este projeto.

<table>
  <tr>
    <td align="center" width="150px">
      <a href="https://github.com/LeticiaMelo2">
       <img src="https://avatars.githubusercontent.com/Bia-z" width="100px;" alt="Beatriz Caroline" style="border-radius: 50%;"/><br>
        <sub>
          <strong>BEATRIZ CAROLINE MORENO TAVARES</strong>
        </sub>
      </a>
    </td>
    <td>
      <h3>Backend, Frontend, Banco de Dados e Arquitetura</h3>
      <p>
        Beatriz foi responsável pela arquitetura do fluxo de operador, e correções do front-end e do back-end no geral, e a integração com o banco de dados MySQL.
      </p>
    </td>
  </tr>
</table>

---


