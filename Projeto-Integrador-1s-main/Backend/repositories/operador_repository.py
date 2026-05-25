#funções que acessam o bd para buscar os operadores

from database.connection import get_db #importa o get_db da pasta database/connection.py, retorna conexão c bd
from models.operador import Operador #importa a classe Operador do models
from mysql.connector import Error #importa a classe de rros da biblioteca do mysql, que podem acontecer em relação a conexão

class OperadorRepository: 
    
    def buscar_por_email(self, email: str): #criação do método, que recebe a si mesmo, e o email em forma de string
        conn = get_db() #chama get_db
        cursor = conn.cursor(dictionary=True) #cria um cursor a partir da conexão (é um objeto q executa comandos do SQL)
        
        try:
            sql = "SELECT * FROM operadores WHERE email = %s" #cria ums str com o comando SQL, %s é um placeholder, sendo substituído pelo email fornecido
            cursor.execute(sql, (email,)) #executa o comando SQL, o email fica nesse formato para substituir os placeholders
            resultado = cursor.fetchone() #pega o resultado da consulta e retorna um dicionário com os dados encontrados, guardando na variável resultado
            
            if resultado: #se achar
                return Operador( #retorna um objeto da classe Operador, com os dados do banco
                    id=resultado['id'], #pega o valor da coluna id e passa pro objeto
                    nome=resultado['nome'], #pega o nome e passa
                    email=resultado['email'] #pega o email e passa
                )
            return None #se n achar retorna none
            
        except Error as e: #captura erros do tipo Error
            print(f"Erro ao buscar operador: {e}") #{e} é uma variável, que a biblioteca do MySQL guarda erros como falha na conexão, tabela errada/n existe
            return None #retorna none qndo a busca falha
        finally: #finally é um bloco que smepre executado, tendo erro ou não
            cursor.close() #fecha o cursos, liberando o bd