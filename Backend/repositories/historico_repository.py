from database.connection import get_db
from models.historico import Historico
from mysql.connector import Error

class HistoricoRepository:

    @staticmethod
    def criar(historico):
        conn = get_db()
        cursor = conn.cursor()

        try:
            sql = """
            INSERT INTO historico
            (solicitacao_id, usuario_id, acao, descricao)
            VALUES (%s, %s, %s, %s)
            """

            valores = (
                historico.solicitacao_id,
                historico.usuario_id,
                historico.acao,
                historico.descricao
            )

            cursor.execute(sql, valores)
            conn.commit()

        except Error as e:
            print(f"Erro ao criar histórico: {e}")
        finally:
            cursor.close()

    @staticmethod
    def listar_por_solicitacao(solicitacao_id):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = """
            SELECT *
            FROM historico
            WHERE solicitacao_id = %s
            ORDER BY data DESC
            """

            cursor.execute(sql, (solicitacao_id,))
            return cursor.fetchall()

        except Error as e:
            print(f"Erro ao buscar histórico: {e}")
            return []
        finally:
            cursor.close()