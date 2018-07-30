from classes.usuario import Usuario


class Admin_sistema(Usuario):
    def create_admin(self):
        self.nome = input("Nome: ")
        self.cpf = input("CPF: ")
        self.endereco = input("Endereço: ")
        self.data_nasc = input("Data de Nascimento: ")
        self.senha = input("Senha: ")




