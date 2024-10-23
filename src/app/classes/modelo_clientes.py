class Clientes: 
    def __init__(self, nome: str, cpf: str, idade: int, email: str=None, telefone: str=None, endereco: str="", profissao: str=""):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.profissao = profissao
        
    def atualizar_dados(self, idade=None, email=None, telefone=None, endereco=None, profissao=None):
        try: 
            
            if idade:
                self.idade = idade
            if email:
                self.email = email
            if telefone:
                self.telefone = telefone
            if endereco:    
                self.endereco = endereco
            if profissao:    
                self.profissao = profissao
                
            #Validação para que ao menos um meio de contato seja fornecido                      
            if not email and not telefone and not self.email and not self.telefone:
                raise ValueError("É necessário fornecer pelo menos um meio de contato: [e-mail] ou [telefone]")
            
        except ValueError as ve:
            print(f'Erro de validação: {ve}')