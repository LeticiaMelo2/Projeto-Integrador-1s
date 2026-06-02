
<div align="center">
    <h1>Sistema de Controle de Solicitações Corporativas (SCSC)</h1>
</div>

---

<h2 id="desc"> 📖 Descrição Geral</h2>

O **SCSC** é uma plataforma web desenvolvida para digitalizar e organizar o gerenciamento de solicitações internas em ambiente corporativo. O sistema permite que colaboradores registrem solicitações, acompanhem seu andamento e que operadores gerenciem e atualizem o status dessas demandas, substituindo métodos informais como e-mails e anotações descentralizadas.

---

<h2 id="func"> 🚀 Funcionalidades</h2>

### 🔹 Cadastro e Login
- Registro de usuários com nome, sobrenome, e-mail e senha;
- Autenticação com redirecionamento automático conforme o perfil (usuário comum ou operador).

### 🔹 Abertura de Solicitações
- Registro de solicitações com título, descrição, impacto e urgência;
- Classificação automática de prioridade (Baixa, Média ou Alta) com base nos fatores informados.

### 🔹 Acompanhamento de Solicitações
- Listagem das solicitações do usuário com filtro por status;
- Cancelamento de solicitações abertas pelo próprio usuário.

### 🔹 Dashboard do Operador
- Visualização de todas as solicitações com filtros por status, prioridade e usuário;
- Atualização de status (Aberta → Em andamento → Finalizada);
- Estatísticas com total de solicitações por status e por prioridade.

### 🔹 Histórico e Comentários
- Registro automático de ações no histórico de cada solicitação;
- Canal de comunicação entre usuários e operadores via comentários.

---

<h2 id="arq"> 📐 Arquitetura do Projeto</h2>

O projeto adota uma arquitetura em camadas, separando as responsabilidades em módulos bem definidos:

### 🔹 Models
- Representam as entidades do sistema (Usuario, Solicitacao, Historico, Comentario);
- Definem os atributos de cada entidade.

### 🔹 Repositories
- Responsáveis pelo acesso ao banco de dados;
- Executam queries SQL puras para consultar, inserir e atualizar dados.

### 🔹 Services
- Contêm as regras de negócio do sistema;
- Exemplos: classificação automática de prioridade, autenticação, estatísticas.

### 🔹 Routes
- Definem os endpoints da aplicação Flask;
- Recebem as requisições, acionam os services/repositories e retornam as respostas.

### 🔄 Fluxo de Operação:
1. O **usuário** interage com a **interface web** (HTML/CSS/JS);
2. A **rota Flask** recebe a requisição e aciona o **service** correspondente;
3. O **repository** executa a query no **banco de dados MySQL**;
4. O resultado é retornado e exibido ao usuário.

### 🎯 Benefícios da arquitetura:
- **Separação de responsabilidades**: cada camada tem um papel claro;
- **Manutenibilidade**: facilita a correção e evolução do código;
- **Escalabilidade**: organização que permite adicionar novas funcionalidades com facilidade.

---

<h2 id="regra"> ⚖️ Regra de Classificação de Prioridade</h2>

A prioridade é calculada automaticamente com base nos fatores **Impacto** e **Urgência**, informados pelo usuário na abertura da solicitação:

| Impacto | Urgência | Prioridade |
|---------|----------|------------|
| Alta    | Alta     | Alta       |
| Alta    | Média    | Alta       |
| Média   | Alta     | Alta       |
| Alta    | Baixa    | Média      |
| Média   | Média    | Média      |
| Baixa   | Alta     | Média      |
| Média   | Baixa    | Baixa      |
| Baixa   | Média    | Baixa      |
| Baixa   | Baixa    | Baixa      |

---

<h2 id="tech"> 🛠️ Tecnologias Utilizadas</h2>

<table>
  <tr>
    <th>Categoria</th>
    <th>Tecnologia</th>
    <th>Descrição</th>
  </tr>
  <tr>
    <td>Linguagem Backend</td>
    <td>Python</td>
    <td>Linguagem principal para desenvolvimento do back-end.</td>
  </tr>
  <tr>
    <td>Framework Backend</td>
    <td>Flask</td>
    <td>Framework minimalista para criação de aplicações web em Python.</td>
  </tr>
  <tr>
    <td>Linguagem Frontend</td>
    <td>JavaScript</td>
    <td>Linguagem para adicionar interatividade ao frontend.</td>
  </tr>
  <tr>
    <td>Linguagem de Estilo</td>
    <td>CSS</td>
    <td>Linguagem para definição de estilos e layouts das páginas web.</td>
  </tr>
  <tr>
    <td>Linguagem de Estrutura</td>
    <td>HTML5</td>
    <td>Linguagem de marcação para estruturar o conteúdo das páginas web.</td>
  </tr>
  <tr>
    <td>Banco de Dados</td>
    <td>MySQL</td>
    <td>Sistema de gerenciamento de banco de dados relacional.</td>
  </tr>
  <tr>
    <td>Ferramenta de Banco de Dados</td>
    <td>MySQL Workbench</td>
    <td>Ferramenta para gerenciamento e modelagem do banco de dados.</td>
  </tr>
  <tr>
    <td>Controle de Versão</td>
    <td>Git e GitHub</td>
    <td>Sistema de controle de versão distribuído.</td>
  </tr>
  <tr>
    <td>IDE</td>
    <td>PyCharm / VS Code</td>
    <td>IDEs utilizadas para o desenvolvimento do projeto.</td>
  </tr>
</table>

---

<h2 id="estrutura"> 📁 Estrutura do Projeto</h2>

Projeto-Integrador-1s/
├── Backend/
│   ├── database/
│   │   └── connection.py
│   ├── forms/
│   │   └── usuario_forms.py
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
│   ├── routes/
│   │   ├── historico_routes.py
│   │   ├── operador_routes.py
│   │   └── usuario_routes.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── classificacao_service.py
│   │   ├── comentario_service.py
│   │   ├── estatistica_service.py
│   │   ├── historico_service.py
│   │   └── solicitacao_service.py
│   ├── .env
│   ├── .env.example
│   ├── config.py
│   ├── main.py
│   └── requirements.txt
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

---

<h2 id="install"> ⚙️ Como Executar</h2>

### Pré-requisitos
- Python 3.10+
- MySQL 8.x
- Git

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/LeticiaMelo2/Projeto-Integrador-1s.git
cd Projeto-Integrador-1s
```

**2. Crie e ative o ambiente virtual:**
```bash
cd Backend
python -m venv .venv
.venv\Scripts\activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Configure o arquivo `.env`:**
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=nome_do_banco

**5. Crie o banco de dados:**
- Abra o MySQL Workbench e execute o script SQL disponível na pasta `Backend/sql/`.

**6. Execute o sistema:**
```bash
python main.py
```

**7. Acesse no navegador:**
http://127.0.0.1:5000

---

<h2 id="colab"> 🤝 Colaboradores</h2>

Um agradecimento especial a todas as pessoas que contribuíram para este projeto.

<table>
  <tr>
    <td align="center" width="150px">
      <a href="https://github.com/LeticiaMelo2">
        <img src="https://avatars.githubusercontent.com/LeticiaMelo2" width="100px;" alt="Beatriz Caroline" style="border-radius: 50%;"/><br>
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


