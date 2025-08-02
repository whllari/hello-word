NOME_PROGRAMA = "AGENDA DE CONTATOS"

agenda = [] # lista para armazenar os contatos

def cadastrar_contato(nome):
    agenda.append(nome) # adiciona o contato á agenda 
    print(f"Contato '{nome}' cadastrado com sucesso!")

def listar_contatos():
    print("Lista de contatos")
    print(agenda)

def remover_contato():
    contato = input("Qual contato deseja remover da agenda: ")
    if contato in agenda:
        agenda.remove(contato) #remove o contato da agenda
        print(f"Contato {contato} removido com sucesso")
    else:
        print(f"Contato {contato} não encontrado na agenda")

def main():
    while True:
        print("")
        print(NOME_PROGRAMA)
        print("-" * 50)
        print("Menu: ")
        print("1.Cadastrar Contato")
        print("2.Listar Contatos")
        print("3.Remover Contato")
        print("4.Sair")
        print("-" * 50)
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite um nome para incluir na agenda: ")
            cadastrar_contato(nome)
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            remover_contato()
        elif opcao == '4':
            break
        else:
            print("Opção invalida, tente novamente")


if __name__ == "__main__":
    main()
