from database.connection import get_db
from models.historico import Historico


class HistoricoRepository:

    @staticmethod
    def criar(historico):
        conn = get_db()
        cursor = conn.cursor()

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

        cursor.close()
        conn.close()


    @staticmethod
    def listar_por_solicitacao(solicitacao_id):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        sql = """
        SELECT *
        FROM historico
        WHERE solicitacao_id = %s
        ORDER BY data DESC
        """

        cursor.execute(sql, (solicitacao_id,))
        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultado