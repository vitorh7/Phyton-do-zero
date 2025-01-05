###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.22.
# data: 05/01/2025
###################
while True:
	tabuada = 1
	operacao = int(input("Digite um número para a tabuada:\n 0 para Sair.\n 1 para Adição.\n 2 para subtração.\n 3 para divisão.\n 4 para multiplicação.\n "))
	if operacao == 1:
		while tabuada <=10:
			numero=1
			while numero <=10:
				print(f"{tabuada}+{numero}={tabuada+numero}.")
				numero += 1
			tabuada+=1
	elif operacao == 2:
		while tabuada <=10:
			numero=1
			while numero <=10:
				print(f"{tabuada}-{numero}={tabuada-numero}.")
				numero += 1
			tabuada+=1
	elif operacao ==3:
		while tabuada <=10:
			numero=1
			while numero <=10:
				print(f"{tabuada}/{numero}={tabuada/numero: .2f}")
				numero += 1
			tabuada+=1
	elif operacao ==4:
		while tabuada <=10:
			numero=1
			while numero <=10:
				print(f"{tabuada}*{numero}={tabuada*numero}.")
				numero += 1
			tabuada+=1
	elif operacao == 0:
		break
	else:
		print("Digite um valor válido!!")