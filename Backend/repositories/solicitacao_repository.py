from database.connection import get_db
from models.solicitacao import Solicitacao
from mysql.connector import Error

class SolicitacaoRepository:

    def criar(self, user_id: int, titulo: str, descricao: str, impacto: str, urgencia: str, prioridade: str, status_id: int):
        conn = get_db()
        cursor = conn.cursor()

        try:
            sql = """
                INSERT INTO ocorrencias (user_id, titulo, descricao, impacto, urgencia, prioridade, status_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (user_id, titulo, descricao, impacto, urgencia, prioridade, status_id))
            conn.commit()
            return True

        except Error as e:
            print(f"Erro ao criar solicitação: {e}")
            return False
        finally:
            cursor.close()

    def buscar_por_usuario(self, user_id: int, filtro: str = 'todos'):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        try:
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
            return cursor.fetchall()

        except Error as e:
            print(f"Erro ao buscar solicitações: {e}")
            return []
        finally:
            cursor.close()

    def buscar_todas(self, status=None, prioridade=None, usuario_id=None):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        try:
            query = """
                    SELECT o.id, o.titulo, o.descricao, s.nome AS status, o.prioridade, u.first_name, u.last_name
                    FROM ocorrencias o
                             JOIN status s ON o.status_id = s.id
                             JOIN usuarios u ON o.user_id = u.id
                    WHERE 1 = 1 \
                    """

            params = []

            # status
            if status and status != "todos":
                query += " AND s.nome = %s"
                params.append(status)

            # prioridade
            if prioridade and prioridade != "todas":
                query += " AND o.prioridade = %s"
                params.append(prioridade)

            # usuario
            if usuario_id and usuario_id != "todos":
                query += " AND o.user_id = %s"
                params.append(usuario_id)

            cursor.execute(query, tuple(params))
            return cursor.fetchall()

        except Error as e:
            print(f"Erro ao buscar solicitações: {e}")
            return []
        finally:
            cursor.close()

    def atualizar_status(self, ocorrencia_id: int, operador_id: int):
        conn = get_db()
        cursor = conn.cursor()

        try:
            query = """
                UPDATE ocorrencias
                SET operador_id = %s,
                    status_id = 2
                WHERE id = %s
            """
            cursor.execute(query, (operador_id, ocorrencia_id))
            conn.commit()
            return True

        except Error as e:
            print(f"Erro ao atualizar status: {e}")
            return False
        finally:
            cursor.close()

    def fechar(self, ocorrencia_id: int):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        try:
            # verifica o status atual antes de fechar, se tive aberta, ou fechada n vai
            cursor.execute(
                "SELECT s.nome AS status FROM ocorrencias o JOIN status s ON o.status_id = s.id WHERE o.id = %s",
                (ocorrencia_id,))
            ocorrencia = cursor.fetchone()

            if not ocorrencia:
                return False, "Solicitação não encontrada"

            if ocorrencia['status'] != 'em andamento':
                return False, "Só é possível fechar solicitações em andamento"

            cursor.execute("UPDATE ocorrencias SET status_id = 3 WHERE id = %s", (ocorrencia_id,))
            conn.commit()
            return True, "Solicitação fechada com sucesso"

        except Error as e:
            print(f"Erro ao fechar solicitação: {e}")
            return False, "Erro ao fechar solicitação"
        finally:
            cursor.close()