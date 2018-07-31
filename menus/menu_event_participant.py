from classes.event import *


def event_participant(user, events):
    option = None

    while option != 5:

        print("-- Menu do Participante --")
        print("Bem vindo(a) {}".format(user.name))
        print("1 - Alterar dados pessoais")
        print("2 - Listar eventos já inscritos")
        print("3 - Detalhar evento")
        print("4 - Realizar a inscrição em evento")
        print("5 - Deslogar")
        option = int(input())

        if option == 1:
            print("OBS: O CPF não pode ser trocado")
            user.change_data_user()
            print("Dados alterados com sucesso! ")

        elif option == 2:
            get_user_events(events, user.cpf)

        elif option == 3:
            get_event_details(events, input("DIgite a sigla do evento: "))

        elif option == 4:
            register_user_in_event(events, user.cpf)

        elif option == 5:
            option = 5
