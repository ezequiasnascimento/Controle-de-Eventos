from classes import *
def apresentacao():
    print("1 - Criar conta")
    print("2 - Realizar login")
    print("3 - Sair do sistema")
usuarios = []
while True:
    apresentacao()
    opcao = int(input())
    if opcao == 1:
        print("Criar Conta")
        usuario = Usuario()
        usuario.criar_conta()
        usuarios.append(usuario)
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