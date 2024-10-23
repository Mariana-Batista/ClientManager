from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import DB_CONFIG

def criar_conexao():
    """Cria a conexão com o banco de dados usando SQLAlchemy."""
    url = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
    engine = create_engine(url, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

def inicializar_banco(engine):
    """Cria as tabelas no banco de dados se ainda não existirem."""
    from app.classes.modelo_clientes import Clientes
    from app.classes.modelo_enderecos import Endereco
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()
    
    # Incluindo as classes de modelo na Base
    Base.metadata.create_all(engine)  # Chama este método para criar as tabelas

if __name__ == "__main__":
    session = criar_conexao()
    engine = session.bind  # Obtém o engine da sessão
    inicializar_banco(engine)

