import re

class ValidadorDeDados:
    
    @staticmethod
    def validar_nome(nome):
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
            raise ValueError('O nome deve conter apenas letras do alfabeto.')
        return nome
    
    @staticmethod
    def validar_idade(idade):
        try:
            idade = int(idade)
            
            if idade < 18:
                raise ValueError('A idade inserida é inválida! Deve ser maior que 18 anos.')
        except ValueError:
            raise ValueError('A idade inserida é inválida! Deve ser um número inteiro.')
        return idade
    
    @staticmethod
    def validar_cpf(cpf):
        cpf = cpf.strip()
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError ("Os dados inseridos são inválidos! O CPF deve ter 11 dígitos.")
        return cpf
    
    @staticmethod
    def validar_email(email):
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("E-mail inválido! Verifique o formato.")
        return email
    
    @staticmethod
    def validar_telefone(telefone):
        telefone = telefone.strip()
        if len(telefone) != 11 or not telefone.isdigit():
            raise ValueError ("Os dados inseridos são inválidos! O telefone deve ter 11 dígitos.")
        return telefone
        
    @staticmethod
    def validar_endereco(endereco):
        if not endereco or not any(char.isalnum() for char in endereco):
            raise ValueError("Os dados inseridos são inválidos! Verifique o endereço digitado.")
        return endereco
        
    @staticmethod
    def validar_profissao(profissao):
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", profissao):
            raise ValueError('A profissão deve conter apenas letras do alfabeto.')
        return profissao
        