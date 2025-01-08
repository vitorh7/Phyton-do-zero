###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.25.
# data: 08/01/2025
###################
print("Eai! bem vindo(a) à calculadora de raiz quadrada newtoniana!")
while True:
	menu=int(input("Escolha o menu:\n 0 para parar o programa.\n 1 para calcular a raiz de um número."))
	if menu==0:
		break
	if menu==1:
		numero=float(input("Digite um número:  "))
		if numero <0:
			print(f"Não existe raiz quadrada de número negativo no universo REAL.")
			continue
		base=2
		while (numero - (base*base))>=0.0001:
			p=(base+(numero/base))/2
			base=p
		print(f"A raiz aproximada de {numero} é {p}!")
	else:
		print(f"{menu: .2f} não é um valor válido!")