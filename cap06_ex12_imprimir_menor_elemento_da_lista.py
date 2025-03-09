###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edição 3: ex6.12.
# Data: 09/03/2025
###################
#Programa que percorre uma lista e imprime o menor valor dela
L = [9, 3, 4, 6, 7, 11, 13, 23, 2, 67, 5]
menor = L[0]
for i in L:
   if i < menor:
       menor = i
print(menor)