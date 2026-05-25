from database.connection import get_db
from models.comentario import Comentario
from mysql.connector import Error

class ComentarioRepository:

    def salvar(self, comentario: Comentario):
        conn = get_db()
        cursor = conn.cursor()

        try:
            sql = """
                INSERT INTO comentarios (solicitacao_id, usuario_id, tipo_autor, mensagem)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (
                comentario.solicitacao_id,
                comentario.usuario_id,
                comentario.tipo_autor,
                comentario.mensagem
            ))
            conn.commit()
            return True

        except Error as e:
            print(f"Erro ao salvar comentário: {e}")
            return False
        finally:
            cursor.close()

    @staticmethod
    def listar_por_ocorrencia(solicitacao_id):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = """
                SELECT c.id,
                       c.solicitacao_id,
                       c.usuario_id,
                       c.tipo_autor,
                       c.mensagem,
                       c.criado_em,
                       COALESCE(CONCAT(u.first_name, ' ', u.last_name), o.nome) AS autor_nome
                FROM comentarios c
                         LEFT JOIN usuarios u ON c.tipo_autor = 'usuario' AND c.usuario_id = u.id
                         LEFT JOIN operadores o ON c.tipo_autor = 'operador' AND c.usuario_id = o.id
                WHERE c.solicitacao_id = %s
                ORDER BY c.criado_em ASC
            """
            cursor.execute(sql, (solicitacao_id,))
            return cursor.fetchall()

        except Error as e:
            print(f"Erro ao buscar comentários: {e}")
            return []
        finally:
            cursor.close()
