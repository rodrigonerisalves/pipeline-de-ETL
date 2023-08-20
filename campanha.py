import csv
import time

def limpar_arquivo():
    with open('campanha.csv', 'w', newline='') as arquivo_csv:
        arquivo_csv.truncate()

def cadastrar_cliente():
    contador = 1
    clientes = []

    while contador <= 3:
        nome = input(f"Cadastre o cliente {contador}: ")

        if nome.isalpha() or nome.isspace():
            clientes.append([nome])
            contador += 1
        else:
            print("ATENÇÃO! Opção inválida, digite apenas primeiro nome.")

    with open('campanha.csv', 'a', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerows(clientes)

    print("Todos clientes cadastrados com sucesso!")

def enviar_campanha(mensagem):
    with open('campanha.csv', 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        nomes = [row[0] for row in reader]

        if mensagem == 1:
            for nome in nomes:
                print(f"{nome}! Invista hoje para um futuro ser seguro e estável!, {nome}! Seu futuro financeiro depende disso!")
        elif mensagem == 2:
            for nome in nomes:
                print(f"Oi, {nome}! Investir cérto é a chave para multiplicar seu dinheiro. Não deixe sua grana parada!")
        elif mensagem == 3:
            for nome in nomes:
                print(f"Invista hoje para garantir um futuro seguro e próspero. {nome}! Seu futuro agradece!")

    print("\nCampanha enviada com sucesso! Santander Agradece...")
    time.sleep(5)

def iniciar_sistema():
    limpar_arquivo()
    print("\n\n")
    print("Bem-vindo ao sistema de envio de mensagem de campanha Santander!")

    while True:
        print("\nOpções:")
        print("1 - Cadastrar Clientes")
        print("2 - Enviar Campanha")
        print("3 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("Sistema Free! Permite apenas 3 cadastros para teste.")
            confirmacao = input("Deseja continuar (Y/N)? ")

            if confirmacao.upper() == "N":
                print("Obrigado!")
                iniciar_sistema()
            elif confirmacao.upper() == "Y":
                cadastrar_cliente()
            else:
                print("ATENÇÃO! Opção inválida!")
        elif opcao == "2":
            if not verificar_arquivo():
                print("Favor cadastrar os clientes da opção (1)")
            else:
                print("1 - Invista hoje para um futuro ser seguro e estável!, Seu futuro financeiro depende disso!")
                print("2 - Oi, investir cérto é a chave para multiplicar seu dinheiro. Não deixe sua grana parada!")
                print("3 - Invista hoje para garantir um futuro seguro e próspero. Seu futuro agradece!")
                msg_opcao = input("Escolha a mensagem a ser enviada (1-3): ")

                if msg_opcao not in ["1", "2", "3"]:
                    print("ATENÇÃO! Opção inválida, digite 1, 2 ou 3.")
                else:
                    enviar_campanha(int(msg_opcao))

                    print("=========================================")
                    print("Retornando ao início do sistema em 5 segundos...")
                    print("=========================================")
                    print("\n\n")
                    time.sleep(5)
        elif opcao == "3":
            confirmacao = input("Você deseja sair do sistema (Y/N)? ")

            if confirmacao.upper() == "Y":
                print("Saindo do sistema...")
                break
            elif confirmacao.upper() == "N":
                pass
            else:
                print("ATENÇÃO! Opção inválida!")
        else:
            print("ATENÇÃO! Opção inválida!")

def verificar_arquivo():
    with open('campanha.csv', 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        linhas = list(reader)

        if len(linhas) < 3:
            return False

        for linha in linhas[:3]:
            if not linha[0].strip():
                return False

    return True

# Inicia o sistema
iniciar_sistema()
