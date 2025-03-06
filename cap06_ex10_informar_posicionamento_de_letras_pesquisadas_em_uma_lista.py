###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edição 3: ex6.10.
# Data: 06/03/2025
###################
# Pesquisa de dois valores e dizer onde foram achados na lista.
lista = [1, 15, 7, 27, 39, 7, 15, 4, 6, 55, 45, 32, 65, 66, 66, 2, 1, 1, 8, 9]
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
            print(f"{lista[x]} achado na posição {x}")
            achado = True
        x += 1
    if not achado:
        print("nada encontrado.")