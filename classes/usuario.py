class Usuario(object):
    nome = None
    cpf = None
    endereco = None
    data_nasc = None
    senha = None

    def __init__(self, nome: object = None, cpf: object = None, endereco: object = None, data_nasc: object = None,
                 senha: object = None) -> object:
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.data_nasc = data_nasc
        self.senha = senha

    def criar_conta(self):
        self.nome = input("Nome: ")
        self.cpf = input("CPF: ")
        self.endereco = input("Endereço :")
        self.data_nasc = input("Data de Nascimento: ")
        self.senha = input("Senha: ")
