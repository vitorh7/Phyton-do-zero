###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.14.
# data: 04/01/2025
###################
contador = 1
acumulador = 0
while True:
	num = int(input("Digite um número inteiro: "))
	media = acumulador/contador
	if num == 0:
		break
	acumulador += num
	contador += 1
print(f"Tu digitou {contador} numeros! A soma deles deu {acumulador} e a média aritmética {media: .2f}.")
	