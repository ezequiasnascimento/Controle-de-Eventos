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


def event_report(event_title, events, users, cpf):
    has_events = False

    for i in events:
        if i.title == event_title:
            has_events = True
            if i.cpf_admin_event == cpf:
                print("Nome: {}\nSigla: {}\nLocal: {}".format(i.name_event, i.title, i.local))

                professional_value = i.value_pro
                student_value = i.value_est

                pro_list, est_list = define_by_payment(i.participants, users)

                enum_participants = 1
                print("Profissionais: ")
                if len(pro_list) > 0:
                    for j in pro_list:
                        print("{} - {}".format(enum_participants, j.name))
                        enum_participants += 1
                else:
                    print("Não há profissionais")

                enum_participants = 1
                print("Estudantes: ")
                if len(est_list) > 0:
                    for j in est_list:
                        print("{} - {}".format(enum_participants, j.name))
                        enum_participants += 1
                else:
                    print("Não há Estudantes")

                total_value = (int(len(pro_list)) * float(professional_value)) + (int(len(est_list)) * float(student_value))
                print("Valor total arrecadado: {}".format(total_value))

            else:
                print("Erro: Você não é administrador desse evento")

    if not has_events:
        print("Não existem eventos com essa sigla!")


def define_by_payment(participants, users):
    pro_list = []
    est_list = []

    for i in participants:
        for j in users:
            if i.cpf == j.cpf and i.user_type == 1:
                pro_list.append(j)
            elif i.cpf == j.cpf and i.user_type == 2:
                est_list.append(j)

    return pro_list, est_list
