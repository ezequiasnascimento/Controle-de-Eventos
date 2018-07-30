from classes.participantes import Participante


def menu_admin(users, user):
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

