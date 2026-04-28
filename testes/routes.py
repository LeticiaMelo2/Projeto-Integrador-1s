from flask import app
from testes.main import Flask, render_template, request
from ProjetoHelpDesk import app

#rotas 
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/ticket/<ocorrencia>")
def homepage(ocorrencia):
    return render_template("ticket.html")