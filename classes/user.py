from classes.event import remove_user_from_events


class User(object):
    name = None
    cpf = None
    address = None
    birth = None
    password = None

    def __init__(self,
                 name: object = None,
                 cpf: object = None,
                 address: object = None,
                 birth: object = None,
                 password: object = None) -> object:

        self.name = name
        self.cpf = cpf
        self.address = address
        self.birth = birth
        self.password = password

    def create_account(self, users):
        self.name = input("Nome: ")
        self.cpf = input("CPF: ")

        while verify_cpf(users, self.cpf):
            print("O CPF já está cadastrado tente novamente")
            self.cpf = input("CPF: ")

        self.address = input("Endereço: ")
        self.birth = input("Data de Nascimento: ")
        self.password = input("Senha: ")

    def change_data_user(self) -> object:
        self.name = input("Nome: ")
        self.address = input("Endereço: ")
        self.birth = input("Data de Nascimento: ")
        self.password = input("Senha: ")


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


def remove_user(users, events, cpf):
    list_type = len(users)
    user = None
    i = 1

    while i <= list_type:
        list_users = users[i]
        for j in list_users:
            if j.cpf == cpf:
                user = j
                break

        i += 1

    remove_user_from_events(user, events)

    return user


def verify_event_adm_user_cpf(users, cpf):
    cpf_exists = False

    if users is not None or len(users[2]) != 0:
        for j in users[2]:
            if j.cpf == cpf:
                cpf_exists = True
                break
    else:
        print("Não existem administradores de eventos cadastrados no sistema")

    return cpf_exists


def turn_user_in_adm(users, user_cpf):
    list_type = len(users)

    # A lista 1 é ignorada já que contém os adms
    i = 2

    while i <= list_type:
        list_users = users[i]
        for j in list_users:
            if j.cpf == user_cpf:
                temp = j
                users[i].remove(temp)
                users[1].append(temp)
                break

        i += 1


def verify_user_and_password(users, cpf, password):
    user_is_valid = False
    list_type = len(users)
    i = 1

    while i <= list_type:
        list_users = users[i]
        for j in list_users:
            if j.cpf == cpf and j.password == password:
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
            if j.cpf == cpf and j.password == password:
                user = j
                user_type = i
                break

        i += 1

    return user, user_type
