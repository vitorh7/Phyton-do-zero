###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.8 02/01/2025
###################
num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
contador=1
resultado=0
while contador<=num2:
	contador=contador+1
	resultado=resultado+num1
print(f"{num1}x{num2}={resultado}")
