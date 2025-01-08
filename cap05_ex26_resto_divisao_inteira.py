###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.25.
# data: 08/01/2025
###################
while True:
	print("Bem vindo(a)! Descubra o resto da divisão inteira entre 2 números.")
	dividendo=int(input("Digite o dividendo:  "))
	divisor=int(input("Digite o divisor:  "))
	resto=abs(dividendo)
	divisor_abs=abs(divisor)
	quociente=0
	if divisor==0:
		print("Não existe divisão por 0!")
		continue
	while resto>=divisor_abs:
		resto-=divisor_abs
		quociente+=1
	if dividendo<0 and divisor>0:
		resto=-resto
	print(f" A divisão tem resto {resto}.")
		