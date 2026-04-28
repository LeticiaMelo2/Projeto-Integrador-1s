from flask import Flask, render_template, request
import mysql.connector
from werkzeug.security import check_password_hash

app = Flask(__name__)

cnx = mysql.connector.connect(user = 'BD240226156', #usuario
                              password = 'Qaqyh8', #senha
                              host = '172.16.12.14', #servidor MySql
                              database = 'BD240226156', #banco de dados
                              ) 

cursor = cnx.cursor()          # executa comandos (query, insert, update...)

print("Conectado com sucesso!")

cursor.close() #fecha cursor
cnx.close() #fecha conexão

print("Conexão fechada!")