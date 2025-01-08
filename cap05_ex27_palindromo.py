###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.27.
# data: 08/01/2025
###################
while True:
	x = input("Digite um número ou palavra para saber se é palíndromo ou digite 0 para parar o programa:  ")
	if x=="0":
		break
	tamanho=len(x)
	a=0 
	inicio=x[0+a]
	fim=x[-1-a]
	contador=1
	while contador<=tamanho:
		if inicio!=fim:
			print(f" {x} não é um palíndromo!")
			break
		elif contador==tamanho:
			print(f" {x} é um palíndromo!")
			break
		a+=1
		contador+=1
	