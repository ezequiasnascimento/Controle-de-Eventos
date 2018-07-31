def show_events(events, cpf):
    has_events = False
    enum_list = 1

    for i in events:
        if i.cpf_admin_event == cpf:
            has_events = True
            print("{}. {} - {}".format(enum_list, i.name_event, i.title))
            enum_list += 1

    if not has_events:
        print("Não existem eventos cadastrados no seu usuário")


def remove_user_from_event(events, event_title, cpf):
    # Só é feita a remoção do CPF
    for i in events:
        if i.cpf_admin_event == event_title:
            for j in i.participants:
                if j == cpf:
                    i.participants.remove(j)
                    break


def event_report(event_title, events, cpf):
    has_events = False
    enum_participants = 1

    for i in events:
        if i.title == event_title:
            has_events = True
            if i.cpf_admin_event == cpf:
                print("Nome: {}\nSigla: {}\nLocal: {}".format(i.name_event, i.title, i.local))
                print("Participantes: ")
                for j in i.participants:
                    print("{} - {}".format(enum_participants, j.name))
                    enum_participants += 1

                # TODO Implementar o valor arrecadado por tipo de ingresso

            else:
                print("Erro: Você não é administrador desse evento")

    if not has_events:
        print("Não existem eventos com essa sigla!")
