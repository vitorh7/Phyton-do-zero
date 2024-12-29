#Calculadora de multa por velocidade.
#29/12/24
velocidade=float((input("Digite sua velocidade em km/h")))
if velocidade>80:
	print(f"Sua velociade é: {velocidade: .1f}, acima do limite de 80km/h, deve pagar uma multa de R${(velocidade-80)*5: .2f}.")
elif 70<=velocidade<=80:
	print("Cuidado! Quase acima do limite permitido, se acelerar mais pode ser multado!")
else:
	print("Voce está dentro do limite de velociade")