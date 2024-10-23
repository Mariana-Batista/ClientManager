from app.database.conexao_db import criar_conexao
from app.classes.modelo_clientes import Clientes
from app.classes.modelo_enderecos import Endereco

def adicionar_cliente(cliente_obj):
    session = criar_conexao()
    try:
        session.add(cliente_obj)
        session.commit()
        print("Cliente adicionado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao adicionar cliente: {e}")
    finally:
        session.close()

def buscar_cliente(cpf):
    session = criar_conexao()
    try:
        cliente = session.query(Clientes).filter_by(cpf=cpf).first()
        if cliente:
            return cliente
        else:
            print("Cliente não encontrado.")
    finally:
        session.close()

def atualizar_cliente(cpf, **kwargs):
    session = criar_conexao()
    try:
        cliente = session.query(Clientes).filter_by(cpf=cpf).first()
        if cliente:
            for key, value in kwargs.items():
                setattr(cliente, key, value)
            session.commit()
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado.")
    finally:
        session.close()

def deletar_cliente(cpf):
    session = criar_conexao()
    try:
        cliente = session.query(Clientes).filter_by(cpf=cpf).first()
        if cliente:
            session.delete(cliente)
            session.commit()
            print("Cliente deletado com sucesso!")
        else:
            print("Cliente não encontrado.")
    finally:
        session.close()

def adicionar_endereco(endereco_obj):
    session = criar_conexao()
    try:
        session.add(endereco_obj)
        session.commit()
        print("Endereço adicionado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao adicionar endereço: {e}")
    finally:
        session.close()
