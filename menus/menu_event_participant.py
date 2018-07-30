from classes.usuario import Usuario
def event_participant(user,usuarios):
    print("-- Menu do Participante --")
    print("1 - Alterar dados pessoais")
    print("2 - Listar eventos já inscritos")
    print("3 - Detalhar evento")
    print("4 - Realizar a inscrição em evento")
    print("5 - Deslogar")
    opcao = 0
    while opcao != 5:
        opcao = int(input())
        if opcao == 1:
            print("OBS: O CPF não pode ser trocado")
            user.change_data_user(usuarios)
            print("Dados alterados com sucesso! ")
        elif opcao == 4:
            pass


