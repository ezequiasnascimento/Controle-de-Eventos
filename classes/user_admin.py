from classes.user import User


class UserAdmin(User):
    def create_admin(self):
        self.name = input("Nome: ")
        self.cpf = input("CPF: ")
        self.address = input("Endereço: ")
        self.birth = input("Data de Nascimento: ")
        self.password = input("Senha: ")


def system_report(events, users):
    total_pro, total_est, total_collected = get_participants_by_type(events)

    print("Administradores do Sistema: {}".format(len(users[1])))
    print("Administradores de Eventos: {}".format(len(users[2])))
    print("Participantes Profissionais: {}".format(total_pro))
    print("Participantes EStudantes: {}".format(total_est))
    print("Total de Eventos: {}".format(len(events)))
    print("Total arrecadado: {}".format(total_collected))


def get_participants_by_type(events):
    total_pro = 0
    total_est = 0
    total_collected = 0

    for i in events:
        num_of_pro, num_of_est, total_event_price = get_users_by_type(i.participants,
                                                                      float(i.value_pro),
                                                                      float(i.value_est))
        total_pro = total_pro + num_of_pro
        total_est = total_est + num_of_est
        total_collected = total_collected + total_event_price

    return total_pro, total_est, total_collected


def get_users_by_type(participants, price_pro, price_est):
    num_of_pro = 0
    num_of_est = 0

    for i in participants:
        if i.user_type == 1:
            num_of_pro += 1
        elif i.user_type == 2:
            num_of_est += 1

    return num_of_pro, num_of_est, ((price_pro * num_of_pro) + (price_est * num_of_est))
