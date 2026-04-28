from flask import Flask, render_template, request
import mysql.connector
from werkzeug.security import check_password_hash

app = Flask(__name__)

def conectar_bd():
    return mysql.connector.connect(
                                    user='root',
                                    password='Ll171207',
                                    host='127.0.0.1',
                                    database='teste'
                                    )

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    username = request.form['username']
    password = request.form['password']

    cnx = conectar_bd()
    cursor = cnx.cursor(dictionary=True)

    # CONSULTA NO BANCO
    cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
    usuario = cursor.fetchone()

    cursor.close()
    cnx.close()

    if usuario:
        if usuario['password'] == password:
            return "Login Ok"
        else:
            return "Senha incorreta"
    else: 
        return "Usuário não encontrado"

if __name__ == '__main__':
    app.run(debug=True)