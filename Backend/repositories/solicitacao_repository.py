from database.connection import get_db
from models.solicitacao import Solicitacao
from mysql.connector import Error

class SolicitacaoRepository:

    def criar(self, usuario_id: int, titulo: str, descricao: str, impacto: str, urgencia: str, prioridade: str):
        conn = get_db()
        cursor = conn.cursor()

        try:
            sql = """
                INSERT INTO ocorrencias (usuario_id, titulo, descricao, impacto, urgencia, prioridade)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (usuario_id, titulo, descricao, impacto, urgencia, prioridade))
            conn.commit()
            return True

        except Error as e:
            print(f"Erro ao criar solicitação: {e}")
            return False
        finally:
            cursor.close()

    def buscar_por_usuario(self, usuario_id: int):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "SELECT * FROM ocorrencias WHERE usuario_id = %s"
            cursor.execute(sql, (usuario_id,))
            resultados = cursor.fetchall()
            return resultados

        except Error as e:
            print(f"Erro ao buscar solicitações: {e}")
            return []
        finally:
            cursor.close()

    def buscar_todas(self):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "SELECT * FROM ocorrencias"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            return resultados

        except Error as e:
            print(f"Erro ao buscar solicitações: {e}")
            return []
        finally:
            cursor.close()