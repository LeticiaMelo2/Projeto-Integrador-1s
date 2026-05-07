from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import mysql.connector
from werkzeug.security import check_password_hash, generate_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email

#http://127.0.0.1:5000

#criando a aplicação do flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'

#banco de dados
def conectar_bd():
    return mysql.connector.connect(
                                    user='root',
                                    password='Ll171207',
                                    host='127.0.0.1',
                                    database='dbProjetoIntegrador1'
                                    )

#login
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form.get('email')
    password = request.form.get('password')

    cnx = conectar_bd()
    cursor = cnx.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()

    cursor.close()
    cnx.close()

    if usuario and check_password_hash(usuario['password'], password):
        session['user_id'] = usuario['id']
        session['user_name'] = usuario['first_name']
        session['permissao'] = usuario['permissao_id']
       
    if usuario['permissao_id'] == 1:
            return redirect(url_for('home'))

    elif usuario['permissao_id'] == 2:
            return redirect(url_for('operador'))

    return "Email ou senha incorretos"
    
#cadastro
class RegisterForm(FlaskForm):
    first_name = StringField('Primeiro nome', render_kw={"placeholder": "Nome"}, validators=[DataRequired()])
    last_name = StringField('Sobrenome', render_kw={"placeholder": "Sobrenome"})
    email = StringField('E-mail', render_kw={"placeholder": "E-mail"}, validators=[Email(message='E-mail inválido!'), InputRequired()])
    password = PasswordField('senha',render_kw={"placeholder": "Senha"}, validators=[InputRequired(), EqualTo('confirm', message='As senhas devem ser iguais')])
    confirm = PasswordField('Confirme a senha', render_kw={"placeholder": "Confirme sua senha"})
    submit = SubmitField('CADASTRAR')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():

        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)

        cnx = conectar_bd()
        cursor = cnx.cursor(dictionary=True)

        print("EMAIL RECEBIDO:", email)

        #verifica se já existe
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario_existente = cursor.fetchone()
        
        if usuario_existente:
            cursor.close()
            cnx.close()

            return "Email já cadastrado"

        #salva no banco
        cursor.execute(
            "INSERT INTO usuarios (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email, password)
        )

        cnx.commit()
        cursor.close()
        cnx.close()

        return redirect('/')
    
    return render_template('register.html', form=form)

@app.route('/home')
def home():
    name = session.get('user_name')
    return render_template('home.html', name=name)

def calcular_prioridade(impacto, urgencia):

    tabela = {
        "Alta": 3,
        "Média": 2,
        "Baixa": 1
    }

    soma = tabela.get(impacto, 1) + tabela.get(urgencia, 1)

    if soma >= 6:
        return "Alta"
    elif soma == 5:
        return "Alta"
    elif soma == 4:
        return "Média"
    else:
        return "Baixa"
    
@app.route('/criar_ocorrencia', methods=['POST'])
def criar_ocorrencia():

    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    impacto = request.form.get('impacto')
    urgencia = request.form.get('urgencia')

    prioridade = calcular_prioridade(impacto, urgencia)

    user_id = session.get('user_id')

    status_id = 1

    cnx = conectar_bd()
    cursor = cnx.cursor()


    cursor.execute("""
        INSERT INTO ocorrencias (user_id, titulo, descricao, impacto, urgencia,prioridade, status_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (user_id, titulo, descricao, impacto, urgencia, prioridade, status_id))

    cnx.commit()
    cursor.close()
    cnx.close()

    return redirect(url_for('home'))

@app.route('/ticket')
def ticket():
    return render_template('ticket.html')

@app.route('/ocorrencias')
def ocorrencias():

    filtro = request.args.get('filtro', 'todos')
    user_id = session.get('user_id')

    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT o.id, o.titulo, o.descricao, s.nome AS status
        FROM ocorrencias o
        JOIN status s ON o.status_id = s.id
        WHERE o.user_id = %s
    """

    params = [user_id]

    # adiciona filtro se não for "todos"
    if filtro != "todos":
        query += " AND s.nome = %s"
        params.append(filtro)

    cursor.execute(query, params)

    dados = cursor.fetchall()
    conn.close()

    return render_template("status.html", dados=dados, filtro=filtro)

@app.route('/operador', methods = ['GET', 'POST'])
def operador():

    status = request.args.get("status")
    prioridade = request.args.get("prioridade")


    conn = conectar_bd()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        ocorrencia_id = request.form.get("ocorrencia_id")
        operador_id = session.get('user_id')

        query = """
            UPDATE ocorrencias
            SET operador_id = %s,
                status_id = 2
            WHERE id = %s
        """
        cursor.execute(query, (operador_id, ocorrencia_id))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('operador'))

    status = request.args.get("status")
    prioridade = request.args.get("prioridade")

    query = """
        SELECT o.id, o.titulo, o.descricao, s.nome AS status, o.prioridade
        FROM ocorrencias o
        JOIN status s ON o.status_id = s.id
        WHERE 1=1
    """

    params = []


    #todo arrumar esse filtro que ta bugado
    # status
    if status and status != "todos":
        query += " AND o.status_id = %s"
        params.append(status)

    # prioridade
    if prioridade and prioridade != "todas":
        query += " AND o.prioridade = %s"
        params.append(prioridade)

    print(query)
    print(params)

    cursor.execute(query, tuple(params))
    resultado = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("operador.html", dados=resultado)

#executando o servidor
if __name__ == '__main__':
    app.run(debug=True)
    
