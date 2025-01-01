#Exercício de Lógica Python
#31/12/24
limite = int(input("Digite um número limite interio: "))
escolha = input("Escolha contar par ou ímpar?: ")
x=1
if escolha=="par":
	while x<=limite:
		if x%2==0:
			print(x)
		x=x+1
elif escolha=="ímpar":
	while x<=limite:
		if x%2!=0:
			print(x)
		x=x+1
else:
	print("Digite um valor válido!")
