###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edição 3: ex6.3.
# Data: 16/01/2025
###################

# Inicialização das listas vazias
l1 = []  # Primeira lista fornecida pelo usuário
l2 = []  # Segunda lista fornecida pelo usuário
l3 = []  # Combinação das duas listas
l4 = []  # Lista final sem valores duplicados

print("Bem vindo(a)!")
# Primeiro loop: adiciona valores à primeira lista (l1)
while True:
    n = input("Valor para primeira lista (0 para parar): ")  # Solicita entrada do usuário
    if n == "0":  # Encerra o loop se o usuário digitar 0
        break
    l1.append(n)  # Adiciona o valor à primeira lista

# Segundo loop: adiciona valores à segunda lista (l2)
while True:
    n = input("Valor para segunda lista (0 para parar): ")  # Solicita entrada do usuário
    if n == "0":  # Encerra o loop se o usuário digitar 0
        break
    l2.append(n)  # Adiciona o valor à segunda lista

# Combinação das duas listas em l3
# Neste ponto, l3 pode conter valores duplicados
l3 = l2 + l1

# Inicializa o índice para percorrer l3
x = 0

# Loop para verificar e eliminar duplicatas
while x < len(l3):  # Enquanto o índice x for menor que o tamanho de l3
    if l3[x] not in l4:  # Verifica se o elemento atual de l3 ainda não está em l4
        l4.append(l3[x])  # Adiciona o elemento em l4, se for único
#Usar .extend fragmenta strings como "gggg" em ['g', 'g', 'g', 'g'], causando repetição mesmo passando pelo verificador if.
    x += 1  # Atualiza o índice para verificar o próximo elemento de l3

# Exibe a lista final sem duplicatas
print(f"{l4}")
