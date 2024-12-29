#Programacao de uma calculadora com 6 operacoes basicas: soma, subtracao, divisao, multiplicao, potenciacao e radiciacao.
#nome: Vitor
#data: 29/12/3024
#pydroid3
operacao=input("Escolha uma operacao: soma, subtrair, dividir, multiplicar, potencia e raiz: ")
if operacao=="soma":
	num1=float(input("Digite um numero: "))
	num2=float(input("Digite outro numero: "))
	print(f"O resultado deu: {num1+num2: .2}")
elif operacao=="subtrair":
    num1=float(input("Digite o numero a ser subtraido: "))
    num2=float(input("Digite o valor que deseja subtrair: "))
    print(f"O resultado deu: {num1-num2: .2}")
elif operacao=="dividir":
    num1=float(input("Digite o numerador: "))
    num2=float(input("Digite o denominador: "))
    if num2==0:
    	print("Nao pode dividir por zero ahaha!" )
    else:
    	print(f"O resultado deu: {num1/num2: .2}")
elif operacao=="multiplicacao":
    num1=float(input("Digite um numero: "))
    num2=float(input("Digite outro numero: "))
    print(f"O resultado deu: {num1*num2: .2}")
elif operacao=="potencia":
    num1=float(input("Digite o valor da base: "))
    num2=float(input("Digite o valor do expoente: "))
    print(f"O resultado deu: {num1**num2: .2}")
elif operacao=="raiz":
    num1=float(input("Digite o radicando: "))
    num2=float(input("Digite o radical: "))
    if num2==0:
    	print("Radical nao pode ser zero hahahah!")
    else:
    	print(f"O resultado deu: {num1**1/num2: .2}")
else:
	print("Digite uma entrada valida!")