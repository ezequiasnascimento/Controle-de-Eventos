from classes.usuario import turn_user_in_adm


def menu_admin(users, user):
    print("-- Menu Administrador do Sistema --")
    print("1 - Cadastrar administrador de sistema")
    print("2 - Cadastrar administrador de evento")
    print("3 - Cadastrar evento")
    print("4 - Remover evento")
    print("5 - Remover usuário")
    print("6 - Listar eventos")
    print("7 - Exibir relatórios do sistema")
    print("8 - Exibir relatório por evento")
    print("9 - Deslogar")
    option = int(input("Selecione a opção: "))

    if option == 1:
        user_cpf = input("Informe o CPF de quem você gostaria de tornar administador: ")
        turn_user_in_adm(users, user_cpf)
