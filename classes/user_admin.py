from classes.user import User


class UserAdmin(User):
    def create_admin(self):
        self.name = input("Nome: ")
        self.cpf = input("CPF: ")
        self.address = input("Endereço: ")
        self.birth = input("Data de Nascimento: ")
        self.password = input("Senha: ")


def system_report(events, users):
    print("No momento há ", len(users[1]), " Administradores do Sistema")
    print("Administradores de Eventos: ", len(users[2]))
    print("Participantes de Eventos: ", len(users[3]))
