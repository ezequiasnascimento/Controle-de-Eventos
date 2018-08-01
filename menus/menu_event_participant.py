from classes.event import *


def event_participant(user, events):
    option = None

    while option != 5:

        print("\n-- Menu do Participante --")
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
            get_event_details(events, input("Digite a sigla do evento: "))

        elif option == 4:
            event = get_event(events, input("Digite a sigla do evento: "))

            if event is not None:
                event.event_viewer_without_users()

                if not user_exist_in_list(event.participants, user.cpf):
                    print("\n-- Ingressos --")
                    print("1 - Profissional: {}".format(event.value_pro))
                    print("2 - Estudante:    {}".format(event.value_est))
                    pay_type = int(input("Digite o tipo de Ingresso: "))
                    register_user_in_event(event, user.cpf, pay_type)

                else:
                    print("O usuário já está cadastrado no evento")

        elif option == 5:
            option = 5
