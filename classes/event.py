class Event(object):
    name_event = None
    title = None
    description = None
    local = None
    start_date = None
    end_date = None
    cpf_admin_event = None
    value_pro = None
    value_est = None
    participants = []

    def __init__(self,
                 name_event=None,
                 title=None,
                 description=None,
                 local=None,
                 start_date=None,
                 end_date=None,
                 cpf_admin_event=None,
                 valor_pro=None,
                 valor_estu=None, participantes=[]):

        self.name_event = name_event
        self.title = title
        self.description = description
        self.local = local
        self.start_date = start_date
        self.end_date = end_date
        self.cpf_admin_event = cpf_admin_event
        self.value_pro = valor_pro
        self.value_est = valor_estu
        self.participants = []

    def create_event(self, users):
        self.name_event = input("Nome do evento: ")
        self.title = input("Digite uma sigla: ")
        self.description = input("De uma breve descricao do evento: ")
        self.local = input("Informe o local: ")
        self.start_date = input("Data de inicio: ")
        self.end_date = input("Data do fim do evento: ")
        self.cpf_admin_event = input("Informe o CPF do adiministrador do evento: ")

        from classes.user import verify_event_adm_user_cpf
        while not verify_event_adm_user_cpf(users, self.cpf_admin_event):
            print("Não existe administrador de evento com esse CPF cadastrado!")
            self.cpf_admin_event = input("Informe o CPF do adiministrador do evento: ")

        self.value_pro = input("Informe o valor para participantes profissional: ")
        self.value_est = input("Informe o valor para estudantes: ")
        self.participants = []

    def event_viewer(self):
        print("Nome: ", self.name_event)
        print("Sigla: ", self.title)
        print("Descrição :", self.description)
        print("Local: ", self.local)
        print("Data de inicio:", self.start_date)
        print("Data de fim: ", self.end_date)
        print("CPF do adiministrador do evento: ", self.cpf_admin_event)
        print("Valor do participante profissional: ", self.value_pro)
        print("Valor de participante estudante: ", self.value_est)

        for x in self.participants:
            print("Nome: ", x.nome, "CPF: ", x.cpf)


def remove_user_from_events(event, events):
    pass


def list_events(events):
    cont = 0
    for x in events:
        print("Evento de Numero ", cont, " Sigla: ", x.title, " Nome: ", x.name_event)
