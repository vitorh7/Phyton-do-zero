###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex6.2.
# Data: 09/01/2025
###################
# Loop principal que mantém o programa ativo até que o usuário escolha sair
while True:
    # Exibe menu e solicita ao usuário que escolha uma opção
    menu = int(input("Bem vindo(a)! Digite:\n 1 para iniciar.\n 0 para fechar o programa.\n "))
    if menu == 0:  # Opção para encerrar o programa
        break
    if menu == 1:  # Opção para iniciar a operação com listas
        l1 = []  # Inicializa a primeira lista
        # Loop para preencher a primeira lista
        while True:
            valor = input("Valor lista 1, para ir para próxima digite 0:  ")
            if valor == "0":  # Condição para sair do loop
                break
            l1.append(valor)  # Adiciona o valor à lista 1

        l2 = []  # Inicializa a segunda lista
        # Loop para preencher a segunda lista
        while True:
            valor = input("Valor para lista 2, para ir para terminar digite 0:  ")
            if valor == "0":  # Condição para sair do loop
                break
            l2.append(valor)  # Adiciona o valor à lista 2

        # Combina as duas listas em uma terceira lista
        l3 = l1[:] + l2[:]  # Cria uma nova lista com os elementos de l1 e l2
        print(f"Ao somar a lista 1 e 2, temos uma lista 3: {l3}.")  # Exibe a lista resultante
    else:
        # Mensagem de erro para entradas inválidas no menu
        print(f"{menu} não é um valor válido!\nTente novamente.")