from database.conexao_db import criar_conexao
from mysql.connector import Error
from classes.modelo_clientes import Clientes

def adicionar_cliente(nome, cpf, idade, email=None, telefone=None, endereco=None):
    """Adiciona um novo cliente ao banco de dados."""
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor()
        sql = """INSERT INTO clientes (nome, cpf, idade, email, telefone, endereco)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (nome, cpf, idade, email, telefone, endereco)
        
        try:
            cursor.execute(sql, valores)
            conexao.commit()  # Confirma a transação
            print("Cliente adicionado com sucesso!")
        except Error as e:
            print(f"Erro ao adicionar cliente: {e}")
            conexao.rollback()  # Reverte a transação em caso de erro
        finally:
            cursor.close()
            conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

def buscar_cliente(cpf):
    """Busca um cliente pelo CPF no banco de dados."""
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor()
        sql = "SELECT * FROM clientes WHERE cpf = %s"
        
        try:
            cursor.execute(sql, (cpf,))
            resultado = cursor.fetchone()
            if resultado:
                print("Cliente encontrado:", resultado)
            else:
                print("Cliente não encontrado.")
        except Error as e:
            print(f"Erro ao buscar cliente: {e}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_cliente(cpf, nome=None, idade=None, email=None, telefone=None, endereco=None):
    """Atualiza as informações de um cliente no banco de dados."""
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor()
        sql = "UPDATE clientes SET nome = %s, idade = %s, email = %s, telefone = %s, endereco = %s WHERE cpf = %s"
        valores = (nome, idade, email, telefone, endereco, cpf)
        
        try:
            cursor.execute(sql, valores)
            conexao.commit()  # Confirma a transação
            if cursor.rowcount > 0:
                print("Cliente atualizado no banco de dados.")
            else:
                print("Nenhum cliente encontrado com esse CPF.")
        except Error as e:
            print(f"Erro ao atualizar cliente: {e}")
            conexao.rollback()  # Reverte a transação em caso de erro
        finally:
            cursor.close()
            conexao.close()

def deletar_cliente(cpf):
    """Deleta um cliente do banco de dados."""
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor()
        sql = "DELETE FROM clientes WHERE cpf = %s"
        
        try:
            cursor.execute(sql, (cpf,))
            conexao.commit()  # Confirma a transação
            if cursor.rowcount > 0:
                print("Cliente deletado do banco de dados.")
            else:
                print("Nenhum cliente encontrado com esse CPF.")
        except Error as e:
            print(f"Erro ao deletar cliente: {e}")
            conexao.rollback()  # Reverte a transação em caso de erro
        finally:
            cursor.close()
            conexao.close()
