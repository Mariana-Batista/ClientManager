from app.menu_principal import Menu
from app.database.conexao_db import criar_conexao

def executar_programa():
    menu = Menu()
    menu.executar_programa()
    
def conexao_bd():
    return criar_conexao()

if __name__ == "__main__":
    executar_programa()