from classes.user import User


def event_participant(user, usuarios):
    print("-- Menu do Participante --")
    print("1 - Alterar dados pessoais")
    print("2 - Listar eventos já inscritos")
    print("3 - Detalhar evento")
    print("4 - Realizar a inscrição em evento")
    print("5 - Deslogar")
    option = 0

    while option != 5:
        option = int(input())
        if option == 1:
            print("OBS: O CPF não pode ser trocado")
            user.change_data_user()
            print("Dados alterados com sucesso! ")
        elif option == 4:
            pass
