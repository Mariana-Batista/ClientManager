from scripts.database.conexao import criar_conexao
from gerenciador import GerenciadorDeClientes
from cliente import Clientes

def adicionar_cliente(nome, cpf, idade, email=None, telefone=None, endereco=None):
    conexao = criar_conexao()
    if conexao:
        cursor = conexao.cursor()
        sql = """INSERT INTO clientes (nome, cpf, idade, email, telefone, endereco)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (nome, cpf, idade, email, telefone, endereco)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Cliente adicionado com sucesso!")
        cursor.close()
        conexao.close()
    else:
        print("Não foi possível conectar ao banco de dados.")

def buscar_cliente(cpf):
    # Implemente a lógica para buscar cliente no banco
    pass

def atualizar_cliente(cpf, nome=None, idade=None, email=None, telefone=None, endereco=None):
    """Atualiza as informações de um cliente no banco de dados."""
    cursor = self.conexao.cursor()
    sql = "UPDATE clientes SET nome = %s, idade = %s, email = %s, telefone = %s, endereco = %s WHERE cpf = %s"
    valores = (cliente.nome, cliente.idade, cliente.email, cliente.telefone, cliente.endereco, cliente.cpf)
    
    try:
        cursor.execute(sql, valores)
        self.conexao.commit()  # Confirma a transação
        print("Cliente atualizado no banco de dados.")
    except Error as e:
        print(f"Erro ao atualizar cliente: {e}")
    finally:
        cursor.close()

def deletar_cliente(cpf):
    """Deleta um cliente do banco de dados."""
    cursor = self.conexao.cursor()
    sql = "DELETE FROM clientes WHERE cpf = %s"
    
    try:
        cursor.execute(sql, (cpf,))
        self.conexao.commit()  # Confirma a transação
        print("Cliente deletado do banco de dados.")
    except Error as e:
        print(f"Erro ao deletar cliente: {e}")
    finally:
        cursor.close()