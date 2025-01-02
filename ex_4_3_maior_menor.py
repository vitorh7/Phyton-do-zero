###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex4.3 29/12/2024
###################
velocidade=float((input("Digite sua velocidade em km/h")))
if velocidade>80:
	print(f"Sua velociade é: {velocidade: .1f}, acima do limite de 80km/h, deve pagar uma multa de R${(velocidade-80)*5: .2f}.")
elif 70<=velocidade<=80:
	print("Cuidado! Quase acima do limite permitido, se acelerar mais pode ser multado!")
else:
	print("Voce está dentro do limite de velociade")
