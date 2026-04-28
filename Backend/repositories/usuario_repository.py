from database.connection import get_db
from models.usuario import Usuario
from mysql.connector import Error

class UsuarioRepository:

    def buscar_por_email(self, email: str):
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        try:
            sql = "SELECT * FROM usuarios WHERE email = %s"
            cursor.execute(sql, (email,))
            resultado = cursor.fetchone()

            if resultado:
                return Usuario(
                    id=resultado['id'],
                    first_name=resultado['first_name'],
                    last_name=resultado['last_name'],
                    email=resultado['email'],
                    password=resultado['password']
                )
            return None

        except Error as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
        finally:
            cursor.close()

    def criar(self, first_name: str, last_name: str, email: str, password: str):
        conn = get_db()
        cursor = conn.cursor()

        try:
            sql = "INSERT INTO usuarios (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (first_name, last_name, email, password))
            conn.commit()
            return True

        except Error as e:
            print(f"Erro ao criar usuário: {e}")
            return False
        finally:
            cursor.close()