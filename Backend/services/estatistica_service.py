from database.connection import get_db
from mysql.connector import Error

class EstatisticaService:

    def total_por_status(self):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        try:
            query = """
                SELECT s.nome AS status, COUNT(o.id) AS total
                FROM status s
                LEFT JOIN ocorrencias o ON o.status_id = s.id
                GROUP BY s.id, s.nome
            """
            cursor.execute(query)
            return cursor.fetchall()

        except Error as e:
            print(f"Erro ao buscar estatísticas por status: {e}")
            return []
        finally:
            cursor.close()

    def total_por_prioridade(self):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        try:
            query = """
                SELECT prioridade, COUNT(id) AS total
                FROM ocorrencias
                GROUP BY prioridade
            """
            cursor.execute(query)
            return cursor.fetchall()

        except Error as e:
            print(f"Erro ao buscar estatísticas por prioridade: {e}")
            return []
        finally:
            cursor.close()