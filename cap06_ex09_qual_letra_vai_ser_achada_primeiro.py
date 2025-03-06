###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edição 3: ex6.9.
# Data: 06/03/2025
###################
# Pesquisa de valores em uma lista e dizer qual valor achado primeiro
lista = [1, 15, 7, 27, 39, 3, 5, 6, 8, 12, 13, 14, 15, 17, 32]
while True:
    try:
        p = int(input("Digite o valor a procurar\ntecle 0 para finalizar: "))
        if p == 0:
            break
        v = int(input("Digite outro valor a procurar\ntecle 0 para finalizar: "))
        if p == 0:
            break
    except ValueError:
        print("Digite um número inteiro.")
        continue
    x = 0
    while x < len(lista):
        if lista[x] == p or lista[x] == v:
            print(f"{lista[x]} achado primeiro!")
            break
        x += 1
    else:
        print("nada encontrado.")