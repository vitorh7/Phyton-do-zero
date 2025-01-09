###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex6.1.
# Data: 09/01/2025
###################
# Inicialização de uma lista com 7 posições para armazenar as notas
notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0  # Variável para acumular a soma das notas
x = 0  # Índice para controle do loop

# Loop para receber as 7 notas e calcular a soma
while x < 7:
    notas[x] = float(input(f"Nota {x}:  "))  # Solicita ao usuário a nota correspondente
    soma += notas[x]  # Soma a nota à variável acumuladora
    x += 1  # Incrementa o índice

x = 0  # Reinicia o índice para reutilização no próximo loop

# Loop para exibir as notas formatadas com duas casas decimais
while x < 7:
    print(f"Nota {x}: {notas[x]:6.2f}")  # Exibe a nota da posição x
    x += 1  # Incrementa o índice

# Calcula e exibe a média das notas
print(f"Média: {soma / x:5.2f}")  # Divide a soma pelo total de notas