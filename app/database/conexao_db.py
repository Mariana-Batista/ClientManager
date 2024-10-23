import mysql.connector
from mysql.connector import Error
from config.settings import DB_CONFIG

def criar_conexao():
    """Cria e retorna uma conexão com o banco de dados MySQL."""
    try:
        conexao = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        if conexao.is_connected():
            print("Conexão bem-sucedida ao MySQL")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
