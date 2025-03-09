###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edição 3: ex6.13.
# Data: 09/03/2025
###################
#Programa com a lista e temperaturas Mons, na Bélgica. Tirar a média, o menor e maior valor.

#Menor Valor
L = [-10, -8, 0, 1, 2, 5, -2, -4]
menor = L[0]
for i in L:
   if i < menor:
       menor = i
print(menor)  # Saída: -10

#Maior Valor
maior = L[0]
for i in L:
   if i > maior:
       maior = i
print(maior)  # Saída: 5

#Média
soma = 0
for i in L:
       soma += i
print(f"{soma/len(L):.2f}")  # Saída: -2.00