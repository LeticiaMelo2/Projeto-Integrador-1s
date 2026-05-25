#centrliza a configuração do banco de dados

import os #importa o módulo que acessa variáveis do sistema
from dotenv import load_dotenv #import da função que lê a .env

load_dotenv() #carrega as variáveis da env

class Config:
    DB_HOST = os.getenv('DB_HOST', 'localhost') #pega a variável da .env que se chama 'DB_HOST', se ela existir, se não, usa 'localhost'
    DB_PORT = int(os.getenv('DB_PORT', 3306)) #mesma coisa
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_NAME = os.getenv('DB_NAME', 'BD24022613')