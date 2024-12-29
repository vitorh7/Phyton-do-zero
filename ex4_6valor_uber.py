#Calcular o preço da viagem
#29/12/24
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
