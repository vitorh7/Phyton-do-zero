###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.11, ex 5.12.
# data: 02/01/2025
###################
capital = float(input("Qual é o depósito inicial?:  "))
juros = float(input("Taxa de juros mensal:  "))
tempo = int(input("Quantos meses ficará rendendo?:"   ))
deposito = float(input("Qual valor valor que vai depositar mensalmente?:  "))
contador = 1
montante = capital
while contador <= tempo:
	contador += 1
	montante = montante + deposito + (montante*juros)
	print (f"{contador} mes(es): R${montante: .2f}.")
print (f"Em {tempo} meses, renderá aproximadamente R${montante: .2f}.")
	

