class Usuario(object):
    nome = None
    cpf = None
    endereco = None
    data_nasc = None
    senha = None
    def __init__(self, nome: object = None, cpf: object = None, endereco: object = None, data_nasc: object = None, senha: object = None) -> object:
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

class Evento(object):
    nome_evento = None
    sigla = None
    descricao = None
    local = None
    data_inicio = None
    data_fim = None
    admin_evento = None
    valor_pro = None
    valor_estu = None
    participantes = []
    def __init__(self,nome_evento = None,sigla = None,descricao = None,local = None,data_inicio = None,data_fim = None,admin_evento = None,valor_pro = None,valor_estu = None,participantes = []):
        self.nome_evento = nome_evento
        self.sigla = sigla
        self.descricao = descricao
        self.local = local
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.admin_evento = admin_evento
        self.valor_pro = valor_pro
        self.valor_estu = valor_estu
        self.participantes = []


