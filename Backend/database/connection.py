#gera a conexão com banco de dados

import mysql.connector #importa a biblioteca que permite python e mysql se comunicarem
from mysql.connector import Error #classe erro da biblioteca
from config import Config #importa a classe config, do config.py que tem as credencias do banco

class Database: #cria a classe Database
    _instance = None 
    
    #isso é chamado antes do init, para garantir uma unica instância (conceito Singleton)
    def __new__(cls): #recebe cls (quase mesma coisa que self), porque é criado antes do objeto existir
        if cls._instance is None: #verifica se já tem instanciacriada
            cls._instance = super().__new__(cls) #cria um objeto na memória e guarda em cls._instance
            cls._instance.connection = None #inicializa o connection como none, pra mostrar q n tem conexão aberta
        return cls._instance #retorna a instância recém criada, ou que já existia
    
    def connect(self): #connect recebe ela mesma
        try:
            print(f"Tentando conectar: host={Config.DB_HOST}, port={Config.DB_PORT}, user={Config.DB_USER}, db={Config.DB_NAME}") #print no terminal
            self.connection = mysql.connector.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME,
                use_pure=True
            )
            print("Conectado com sucesso!") #usa as credenciais da .env, passadas para o config
            return self.connection #se der erro retorna ele no terminal
        except Error as e: #guarda o erro na variável e
            print(f"Erro ao conectar: {e}") #printa o erro
            return None #retorna none quando falha
    
    def get_connection(self): 
        if self.connection is None or not self.connection.is_connected():
            return self.connect() #se não tiver conexão anterior, ou tirnha e ela caiu, retorna a função anterior
        return self.connection #se não, retorna a conexão
    
    def close(self):
        if self.connection and self.connection.is_connected(): #verifica se tem alguma conexão ativa
            self.connection.close() #fecha
            self.connection = None #recebe none

def get_db(): #função que repositórios chamam
    db = Database() #recebe a classe anterior, fazendo tudo que foi configurado
    return db.get_connection() #chama a função que retorna a conexão