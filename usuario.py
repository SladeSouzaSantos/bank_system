from conta_corrente import ContaCorrente

class Usuario:
    
    def __init__(self, cpf = None, nome = None, data_nascimento = None, endereco = None, contas: list[ContaCorrente] = []):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = contas

    def criar_usuario(*, cpf, nome, data_nascimento, endereco):
        novo_usuario = Usuario(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco, contas = [])
        return novo_usuario