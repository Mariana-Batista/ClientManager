class Endereco:
    def __init__(self, estado: str, cidade: str, logadouro: str, numero: int=None):
        self.estado = estado
        self.cidade = cidade
        self.logadouro = logadouro
        self.numero = numero
        
    def atualizar_endereco(self, estado, cidade, logadouro, numero=None):
        
        if estado:
            self.estado = estado
        if cidade:
            self.cidade = cidade
        if logadouro:
            self.logadouro = logadouro
        if numero:
            self.numero = numero
        
        