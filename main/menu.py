from classes.participantes import *
from classes.admin_sistema import *
from menus.menu_admin import menu_admin
from menus.menu_event import event_admin
from menus.menu_event_participant import event_participant

usuarios = {1: [], 2: [], 3: []}


def apresentacao():
    print("1 - Criar conta")
    print("2 - Realizar login")
    print("3 - Sair do sistema")


def define_admin():
    while True:
        print("Bem vindo ao gerenciador de eventos!!!")
        print("No momento o sistema está sem um adiministrador")
        print("Por favor digite suas informações para adiministrar o sistema")
        admin_sistema = Admin_sistema()
        admin_sistema.create_account(usuarios)
        usuarios[1].append(admin_sistema)
        print("\n\n\n")
        break


# 1 referencia ao adiministrador do sistema
# 2 referencia ao adiminustrador do evento
# 3 referencia aos participantes
def menu():
    while True:
        apresentacao()
        opcao = int(input())

        if opcao == 1:
            print("Criar Conta")
            participante = Participante()
            participante.create_account(usuarios)
            usuarios[3].append(participante)

        elif opcao == 2:
            print("Realizar login")
            cpf = input("CPF: ")
            senha = input("Senha : ")

            while not verify_user_and_password(usuarios, cpf, senha):
                print("O CPF ou senha são invalidos!")
                cpf = input("CPF: ")
                senha = input("Senha : ")

            user, user_type = get_user_with_type(usuarios, cpf, senha)
            # print("User: {}, User_Type: {}".format(user.nome, user_type))

            if user_type == 1:
                menu_admin(user)
            elif user_type == 2:
                event_admin(user)
            elif user_type == 3:
                event_participant(user)

        elif opcao == 3:
            print("Obrigado por usar o sistema")
            break

        else:
            print("Opção invalida !!!")
        print("\n\n\n")


define_admin()
menu()
