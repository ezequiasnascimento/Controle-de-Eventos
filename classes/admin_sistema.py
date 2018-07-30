from classes.usuario import Usuario


class Admin_sistema(Usuario):
    def create_admin(self):
        self.nome = input("Nome: ")
        self.cpf = input("CPF: ")
        self.endereco = input("Endereço: ")
        self.data_nasc = input("Data de Nascimento: ")
        self.senha = input("Senha: ")

def relatorio_sistema(events,users):
    print("No momento há ",len(users[1])," Administradores do Sistema")
    print("Administradores de Eventos: ",len(users[2]))
    print("Participantes de Eventos: ",len(users[3]))

