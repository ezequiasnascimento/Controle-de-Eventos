from classes.admin_event import *


def event_admin(users, events, user):
    option = None

    while option != 5:
        print("\n-- Menu Administrador de Eventos --")
        print("Bem vindo(a) {}".format(user.name))
        print("1 - Alterar dados pessoais")
        print("2 - Listar eventos")
        print("3 - Desinscrever usuário de evento")
        print("4 - Exibir relatório por evento")
        print("5 - Deslogar")

        option = int(input("Selecione a opção: "))

        if option == 1:
            print("Edição do usuário")
            user.change_data_user()

        elif option == 2:
            show_events(events, user.cpf)

        elif option == 3:
            remove_user_from_event(
                events,
                input("Digite a sigla do evento: "),
                input("Digite o CPF do participante: "))

        elif option == 4:
            event_report(input("Digite a sigla do evento: "), events, user.cpf)

        elif option == 5:
            option = 5

        else:
            print("Opção invalida")
