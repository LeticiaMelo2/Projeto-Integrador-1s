#o repositório é responsável por falar com o bd, o models define a estrutura, mas o repositório faz as ações

from database.connection import get_db
from models.usuario import Usuario
from mysql.connector import Error

class UsuarioRepository:

    def buscar_por_email(self, email: str):
        conn = get_db() #pega a função get_db do connection.py
        cursor = conn.cursor(dictionary=True) #dictionary é True, porque sem ele o bd retorna um tupla, permitindo a gente
                                              #acessar por exemplo resultado['email'], ao invés de resultado[2]
#conn.cursor cria o cursor
        try:
            sql = "SELECT * FROM usuarios WHERE email = %s" #cria a variável sql que vai guardar as informações do usuário com o email escolhido
            cursor.execute(sql, (email,)) #aponta pro banco e executa o SQL passado
            resultado = cursor.fetchone() #pega uma linha

            if resultado: #se realmente existir a linha
                return Usuario(
                    id=resultado['id'],
                    first_name=resultado['first_name'],
                    last_name=resultado['last_name'],
                    email=resultado['email'],
                    password=resultado['password'],
                    permissao_id=resultado['permissao_id']
                ) #monta o objeto e retorna as  informações do usuário
            return None

        except Error as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
        finally: # finally roda sempre, com erro ou sem erro, garantindo que o cursor seja fechado sempre
            cursor.close() #fecha o cursor para evitar desperdício de memória

    def criar(self, first_name: str, last_name: str, email: str, password: str, permissao_id: int = 1):
        conn = get_db()
        cursor = conn.cursor() #não precisa de dictionary true, porque não está retornando nada apenas guardando no bd

        try:
            sql = "INSERT INTO usuarios (first_name, last_name, email, password, permissao_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (first_name, last_name, email, password, permissao_id))
            conn.commit()
            return True

        except Error as e:
            print(f"Erro ao criar usuário: {e}")
            return False
        finally:
            cursor.close()

    def buscar_todos(self):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "SELECT id, first_name, last_name FROM usuarios"
            cursor.execute(sql)
            return cursor.fetchall()

        except Error as e:
            print(f"Erro ao buscar usuários: {e}")
            return []
        finally:
            cursor.close()