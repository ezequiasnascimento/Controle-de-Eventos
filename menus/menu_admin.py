from classes.evento import Evento
from classes.participantes import Participante
from classes.usuario import remove_user


def menu_admin(users, user, events):
    option = None

    while option != 9:
        print("\n-- Menu Administrador do Sistema --")
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
            new_user = Participante()
            new_user.create_account(users)
            users[1].append(new_user)

        elif option == 2:
            print("Digite as informações do novo administrador de eventos")
            new_user = Participante()
            new_user.create_account(users)
            users[2].append(new_user)

        elif option == 3:
            print("Insira as informações do novo evento")
            event = Evento()
            event.criar_evento(users)
            events.append(event)

        elif option == 4:
            pass

        elif option == 5:
            #TODO Finalizar método de remoção
            remove_user(users, events, input("Informe o CPF do usuário que gostaria de remover"))

        elif option == 6:
            pass

        elif option == 7:
            pass

        elif option == 8:
            pass

        elif option == 9:
            option = 9
