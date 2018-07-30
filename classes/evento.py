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

    def __init__(self, nome_evento=None, sigla=None, descricao=None, local=None, data_inicio=None, data_fim=None,
                 admin_evento=None, valor_pro=None, valor_estu=None, participantes=[]):
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

    def criar_evento(self):
        self.nome_evento = input("Nome do evento: ")
        self.sigla = input("digite uma sigla: ")
        self.descricao = input("De uma breve descricao do evento :")
        self.local = input("Informe o local: ")
        self.data_inicio = input("Data de inicio: ")
        self.data_fim = input("data do fim do evento")
        self.admin_evento = input("Informe o adiministrador do evento: ")
        self.valor_pro = input("Informe o valor para participantes profissional: ")
        self.valor_estu = input("Informe o valor para estudantes:")
        self.participantes = []
