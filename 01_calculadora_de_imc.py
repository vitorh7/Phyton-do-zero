#Exercício de Lógica de Programação
#nome: Vitor
#data: 19/12/3024
#pydroid3

altura = float(input("Digite sua altura em metros: "))
#pede altura do usuário
peso = float(input("Digite seu peso em Kg: "))
#pede o peso do usuário
imc = peso/altura**2
#cálculo imc
if imc<16:
	print(f"Seu IMC é {imc: .2f}, isso significa que sua faixa corporal está na magreza grave!")
elif 16<=imc<17:
	print(f"Seu IMC é {imc: .2f}, isso significa que sua faixa corporal está na magreza moderada!")
elif 17<=imc<18.5:
	print(f"Seu IMC é {imc: .2f}, isso significa que sua faixa corporal está na magreza leve!")
elif 18.5<=imc<25:
	print(f"Seu IMC é {imc: .2f}, isso significa que sua faixa corporal está no normal!")
elif 25<=imc<30:
	print(f"Seu IMC é {imc: .2f}, isso significa que sua faixa corporal está no sobrepeso!")
elif 30<=imc<35:
	print(f"Seu IMC é {imc: .2f}, isso significa que sua faixa corporal está na Obseidade 1 (grave)!")
elif 35<=imc<40:
	print(f"Seu IMC é {imc: .2f}, isso significa que sua faixa corporal está na Obsesidade 2 (severa)!")
elif 40<=imc:
	print(f"Seu IMC é {imc: .2f}, isso significa que sua faixa corporal está na Obsedidade 3 (móbida)!")
else:
	print('Algo de errado não está certo ou seu imc não cabe em nenhum espectro.')