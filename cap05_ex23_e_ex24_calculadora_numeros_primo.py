###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.23 e 24.
# Data: 12/01/2025
###################
# Verificador de número primo
# Menu para o usuário
while True:  
    menu = int(input("Escolha: \n0 para fechar o programa \n1 para verificar primo.\n2 para contar n primos\n"))  # Solicita a escolha do usuário  
    if menu == 0:  # Encerra o programa se o usuário digitar 0  
        break  
    elif menu == 1:  # Opção para verificar se um número é primo  
        num = int(input("Digite um número: "))  # Solicita o número para análise  
        if num == 0 or num == 1:  # 0 e 1 não são números primos  
            print(f"{num} não é um número primo!")  
            continue  
        elif num == 2:  # Trata o caso especial do número 2 (único primo par)  
            print(f"{num} é o único primo par!")  
            continue  
        elif num < 0:  # Impede números negativos  
            print(f"Não pode ser valores negativos!")  
            continue  
        elif num % 2 == 0:  # Verifica se o número é par (não é primo, exceto o 2)  
            print("Não é primo.")  
        else:  
            impar = 3  # Inicia a verificação com números ímpares  
            while impar < num:  # Testa divisores ímpares menores que o número  
                if num % impar == 0:  # Se for divisível, não é primo  
                    print("Não é primo.")  
                    break  
                impar += 2  # Incrementa para o próximo número ímpar  
            if impar == num:  # Se nenhum divisor for encontrado, é primo  
                print("É primo!")  
    elif menu == 2:  # Opção para contar os primeiros n números primos  
        n = int(input("Digite n números primos para contar:  "))  # Quantidade de números primos desejados  
        if n <= 0:  # Impede valores inválidos  
            print("Quantidade inválida!")  
            break  
        print("2")  # O número 2 é o primeiro primo  
        if n > 1:  
            primo = 3  # Inicia a verificação a partir do número 3  
            contador = 2  # Já contamos o número 2 como o primeiro primo  
            while contador <= n:  # Conta até atingir o número desejado de primos  
                impar = 3  
                while impar < primo:  # Verifica se o número atual é primo  
                    if primo % impar != 0:  
                        impar += 2  
                        continue  
                    elif primo % impar == 0:  # Não é primo, incrementa para o próximo número  
                        primo += 2  
                        break  
                else:  # Se nenhum divisor for encontrado, o número é primo  
                    print(f"{primo}")  
                    contador += 1  # Incrementa o contador de primos encontrados  
                    primo += 2  # Passa para o próximo número ímpar  
    else:  
        print("Digite um valor válido.")  # Opção inválida no menu