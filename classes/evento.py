


class Evento(object):
    nome_evento = None
    sigla = None
    descricao = None
    local = None
    data_inicio = None
    data_fim = None
    cpf_admin_evento = None
    valor_pro = None
    valor_estu = None
    participantes = []

    def __init__(self, nome_evento=None, sigla=None, descricao=None, local=None, data_inicio=None, data_fim=None,
                 cpf_admin_evento=None, valor_pro=None, valor_estu=None, participantes=[]):
        self.nome_evento = nome_evento
        self.sigla = sigla
        self.descricao = descricao
        self.local = local
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.cpf_admin_evento = cpf_admin_evento
        self.valor_pro = valor_pro
        self.valor_estu = valor_estu
        self.participantes = []

    def criar_evento(self, users):
        self.nome_evento = input("Nome do evento: ")
        self.sigla = input("Digite uma sigla: ")
        self.descricao = input("De uma breve descricao do evento: ")
        self.local = input("Informe o local: ")
        self.data_inicio = input("Data de inicio: ")
        self.data_fim = input("Data do fim do evento: ")
        self.cpf_admin_evento = input("Informe o CPF do adiministrador do evento: ")
        from classes.usuario import verify_event_adm_user_cpf
        while not verify_event_adm_user_cpf(users, self.cpf_admin_evento):
            print("Não existe administrador de evento com esse CPF cadastrado!")
            self.cpf_admin_evento = input("Informe o CPF do adiministrador do evento: ")
        self.valor_pro = input("Informe o valor para participantes profissional: ")
        self.valor_estu = input("Informe o valor para estudantes: ")
        self.participantes = []
    def view_evento(self):
        print("Nome: ",self.nome_evento)
        print("Sigla: ",self.sigla_
        print("Descrição :"self.descricao)
        print("Local: ",self.local)
        print("Data de inicio:" ,self.data_inicio)
        print("Data de fim",self.data_fim)
        print("CPF do adiministrador do evento: ",self.cpf_admin_evento)
        print("Valor do participante profissional",self.valor_pro )
        print("Valor de participante estudante ",self.valor_estu )
        for x in self.participantes:
            print("Nome: ",x.nome,"CPF: ", x.cpf)
def remove_user_from_events(event, events):
    pass
def listar_eventos(events):
    cont = 0
    for x in events:
        print("Evento de Numero ",cont," Sigla: ",x.sigla," Nome: ",x.nome_evento)