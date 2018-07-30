from classes import *
def apresentacao():
    print("1 - Criar conta")
    print("2 - Realizar login")
    print("3 - Sair do sistema")
usuarios = {1:[],2:[],3:[]}
# 1 referencia ao adiministrador do sistema
# 2 referencia ao adiminustrador do evento
# 3 referencia aos participantes
def Menu():
    while True:
        apresentacao()
        opcao = int(input())
        if opcao == 1:
            print("Criar Conta")
            participante = Participante()
            participante.criar_conta()
            usuarios[3].append(participante)

        elif opcao == 2:
            print("Realizar login")
            cpf = input("CPF: ")
            senha = input("Senha : ")
            for x in usuarios:
                if x.cpf == cpf and x.senha == senha:
                    print("logado com sucesso, aqui vai suceder os proximos metodos ")

                else:
                    print("Usuario não encontrado")

        elif opcao == 3:
            print("Obrigado por usar o sistema")
            break
        else:
            print("Opção invalida !!!")
        print("\n\n\n")
while True:
    print("Bem vindo ao gerenciador de eventos!!!")
    print("No momento o sistema está sem um adiministrador")
    print("Por favor digite suas informações para adiministrar o sistema")
    admin_sistema = Admin_sistema()
    admin_sistema.criar_conta()
    usuarios[1].append(admin_sistema)
    print("\n\n\n")
    break
Menu()
