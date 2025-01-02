###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex4.6 28/12/2024
###################
distancia=float(input("Voce vai pedir Uber, qual distancia deseja percorrer em Km?: "))
veiculo=input("Voce vai de carro ou moto?: ")
if distancia<=200:
	if veiculo=="carro" or "Carro":
		print(f"Para uma viagem de {veiculo}, numa distancia de {distancia: .1f}km, custará: R$", distancia*0.5+6)
	elif veiculo=="moto" or "Moto":
		print(f"Para uma viagem de {veiculo}, numa distancia de {distancia: .1f}km, custará: R$", distancia*0.5+3)
	else:
		print("Especifique corretamente o veículo!")	
else:
	if veiculo=="carro" or "Carro":
		print(f"Para uma viagem de {veiculo}, numa distancia de {distancia: .1f}km, custará: R$", distancia*0.45+6)
	elif veiculo=="moto" or "Moto":
		print(f"Para uma viagem de {veiculo}, numa distancia de {distancia: .1f}km, custará: R$", distancia*0.45+3)
	else:
		print("Especifique corretamente o veículo!")
