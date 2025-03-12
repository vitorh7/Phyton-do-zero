#09/03/2025
# Programa que altera o valor das quantidades de vagas de um cinema
# Lista com a quantidade de vagas em cada sala
Salas = [10, 3, 5, 2, 3, 4, 5, 22, 7]

while True:
    try:
        # Solicita a sala que deseja alugar
        escolha = int(input("Digite a sala que deseja alugar (0 para sair):\n"))
        # Verifica se deseja sair
        if escolha == 0:
            break
        # Verifica se a sala escolhida existe
        elif escolha > len(Salas) or escolha < 1:
            print("Sala não existe.")
        # Verifica se a sala escolhida tem vagas
        elif Salas[escolha-1] == 0:
            print("Sala sem vagas.")
        # Se a sala escolhida tem vagas, vai solicitar a quantidade de cadeiras que deseja alugar
        else:
            while True:
                try:
                    # Vai tentar solicitar a quantidade de cadeiras que deseja alugar
                    cadeiras = int(input(f"Vagas disponíveis: {Salas[escolha-1]}, Quantas CADEIRAS deseja alugar? (0 para sair)\n"))
                    # Verifica se deseja sair
                    if cadeiras == 0:
                        break
                    # Verifica se a quantidade de cadeiras é válida, se não for, vai continuar no loop para o usuário tentar novamente
                    elif cadeiras > Salas[escolha-1] or cadeiras < 0:
                        print("Quantidade inválida!")
                        continue
                    # Se a quantidade de cadeiras for válida, vai subtrair a quantidade de cadeiras da sala escolhida e informar a quantidade restante
                    print(f"Pedido feito com sucesso! Você alugou {cadeiras}\ncadeiras na sala {escolha}, restaram {Salas[escolha-1]} cadeiras.")
                    break  # Saída do loop.
                #Se o valor inserido não for um número inteiro, vai informar que o valor é inválido e continuar no loop.
                except ValueError:
                    print("Valor inválido! Por favor, insira um número inteiro.")
    #Se o valor inserido não for um número inteiro, vai informar que o valor é inválido e continuar no loop.
    except ValueError:
        print("Valor inválido! Por favor, insira um número inteiro.")