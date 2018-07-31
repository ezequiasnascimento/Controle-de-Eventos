from classes.user_admin import system_report
from classes.event import *
from classes.participant import Participant
from classes.user import remove_user


def menu_admin(users, user, events):
    option = None

    while option != 9:
        print("\n-- Menu Administrador do Sistema --")
        print("Bem vindo: {}".format(user.name))
        print("1 - Cadastrar administrador de sistema")
        print("2 - Cadastrar administrador de evento")
        print("3 - Cadastrar evento")
        print("4 - Remover evento")
        print("5 - Remover usuário")
        print("6 - Listar eventos")
        print("7 - Exibir relatórios do sistema")
        print("8 - Exibir relatório por evento")
        print("9 - Deslogar\n")
        option = int(input("Selecione a opção: "))

        if option == 1:
            print("Digite as informações do novo administrador")
            new_user = Participant()
            new_user.create_account(users)
            users[1].append(new_user)

        elif option == 2:
            print("Digite as informações do novo administrador de eventos")
            new_user = Participant()
            new_user.create_account(users)
            users[2].append(new_user)

        elif option == 3:
            print("Insira as informações do novo evento")
            event = Event()
            event.create_event(users)
            events.append(event)

        elif option == 4:
            print("Remover Evento")
            print("digite a sigla do evento")
            title = input()
            for x in events:
                if x.title == title:
                    events.remove(x)
            else:
                print("Sigla invalida")

        elif option == 5:
            #TODO Implementar método para remover usuários
            remove_user(users, events, input("Informe o CPF do usuário que gostaria de remover"))

        elif option == 6:
            list_events(events)

        elif option == 7:
            system_report(events, users)

        elif option == 8:
            have_event = False
            title = input("Sigla do evento ")
            print("Relatorio")
            for y in events:
                if y.title == title:
                    have_event = True
                    y.event_viewer()

            if not have_event:
                print("Sigla não encontrada")

        elif option == 9:
            option = 9

        else:
            print("Opção invalida")
