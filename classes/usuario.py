class Usuario(object):
    nome = None
    cpf = None
    endereco = None
    data_nasc = None
    senha = None
    tipo = None

    def __init__(self, nome: object = None, cpf: object = None, endereco: object = None, data_nasc: object = None,
                 senha: object = None, tipo: object = None) -> object:
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.data_nasc = data_nasc
        self.senha = senha
        self.tipo = tipo

    def create_account(self, users):
        self.nome = input("Nome: ")

        self.cpf = input("CPF: ")
        while verify_cpf(users, self.cpf):
            print("O CPF já está cadastrado tente novamente")
            self.cpf = input("CPF: ")

        self.endereco = input("Endereço: ")
        self.data_nasc = input("Data de Nascimento: ")
        self.senha = input("Senha: ")


def verify_cpf(users, cpf):
    cpf_exists = False
    list_type = len(users)
    i = 1

    while i <= list_type:
        list_users = users[i]
        for j in list_users:
            if j.cpf == cpf:
                cpf_exists = True
                break

        i += 1

    return cpf_exists


def verify_user_and_password(users, cpf, password):
    user_is_valid = False
    list_type = len(users)
    i = 1

    while i <= list_type:
        list_users = users[i]
        for j in list_users:
            if j.cpf == cpf and j.senha == password:
                user_is_valid = True
                break

        i += 1

    return user_is_valid


def get_user_with_type(users, cpf, password):
    user = ""
    user_type = ""
    list_type = len(users)
    i = 1

    while i <= list_type:
        list_users = users[i]
        for j in list_users:
            if j.cpf == cpf and j.senha == password:
                user = j
                user_type = i
                break

        i += 1

    return user, user_type