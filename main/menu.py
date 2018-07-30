from classes.participant import *
from classes.user_admin import *
from menus.menu_admin import menu_admin
from menus.menu_event import event_admin
from menus.menu_event_participant import event_participant

# 1 referencia ao adiministrador do sistema
# 2 referencia ao adiminustrador do evento
# 3 referencia aos participantes
users = {1: [], 2: [], 3: []}
events = []


def main_menu():
    print("1 - Criar conta")
    print("2 - Realizar login")
    print("3 - Sair do sistema")


def define_admin():
    while True:
        print("Bem vindo ao gerenciador de eventos!!!")
        print("No momento o sistema está sem um adiministrador")
        print("Por favor digite suas informações para adiministrar o sistema")
        admin_sistema = UserAdmin()
        admin_sistema.create_account(users)
        users[1].append(admin_sistema)
        print("")
        break


def menu():
    while True:
        main_menu()
        option = int(input("Digite a opção: "))

        if option == 1:
            print("Criar Conta")
            participante = Participant()
            participante.create_account(users)
            users[3].append(participante)

        elif option == 2:
            print("Realizar login")
            cpf = input("CPF: ")
            password = input("Senha : ")

            while not verify_user_and_password(users, cpf, password):
                print("O CPF ou senha são invalidos!")
                cpf = input("CPF: ")
                password = input("Senha : ")

            user, user_type = get_user_with_type(users, cpf, password)

            if user_type == 1:
                menu_admin(users, user, events)
            elif user_type == 2:
                event_admin(user)
            elif user_type == 3:
                event_participant(user, users)

        elif option == 3:
            print("Obrigado por usar o sistema")
            break

        else:
            print("Opção invalida !!!")
        print("\n\n\n")


define_admin()
menu()
