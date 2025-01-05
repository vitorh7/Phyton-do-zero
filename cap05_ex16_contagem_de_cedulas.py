###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.20.
# data: 05/01/2025
###################
valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
apagar = valor
while True:
	if atual <= apagar:
		apagar -= atual
		cedulas += 1
	else:
		print(f"{cedulas} cédula(s) de R${atual}")
		if apagar==0:
			break
		elif atual ==100:
			atual =50
		elif atual ==50:
			atual = 20
		elif atual ==20:
			atual=10
		elif atual ==10:
			atual = 1
		elif atual ==1:
			atual =0.5
		elif atual ==0.5:
			atual =0.2
		elif atual ==0.2:
			atual =0.01
		else:
			print("Não há cédulas desse valor :(")
			break
		cedulas = 0
		