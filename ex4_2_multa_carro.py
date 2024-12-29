#Ler 3 números e inprimir o maior e o menor
#29/12/24
num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))
num3=float(input("Digite o terceiro número: "))
if num1>num2 and num3:
	maior=num1
	if num2<num3:
		menor=num2
		print(f"O maior é {maior: .2f} e o menor {menor: .2f}")
	else:
			menor=num3
			print(f"O maior é {maior: .2f} e o menor {menor: .2f}")
elif num2>num1 and num3:
	maior=num2
	if num1<num3:
		menor=num1
		print(f"O maior é {maior: .2f} e o menor {menor: .2f}")
	else:
		menor=num3
		print(f"O maior é {maior: .2f} e o menor {menor: .2f}")
else:
	maior=num3
	if num1<num2:
		menor=num1
	else:
		menor=num2
		print(f"O maior é {maior: .2f} e o menor {menor: .2f}")
		
	