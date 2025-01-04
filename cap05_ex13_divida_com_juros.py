###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.13.
# data: 04/01/2025
###################
divida = float(input("Valor da dívida:  "))
juros = float(input("Juros mensal:  "))
pago = float(input("Pagamento mensal: "))
contador = 1
acumulador = divida
while acumulador>0:
	    if contador>=2:
	    	juros_mes = acumulador*juros
	    	acumulador+=juros_mes-pago
	    else:
	    	acumulador -= pago
	    if acumulador>=divida:
	    	print("Não é possível pagar essa dívida, tente um juros menor ou aumente as parcelas.")
	    	break
	    elif contador >= 50:
	    	print("Tu vai ficar pagando por mais de 50 anos!")
	    	break
	    print(f"{contador} mes: pagou R${pago} e falta R${acumulador: .2f}.")
	    contador += 1
if acumulador<0:
	print(f"Vai demorar {contador} mes(es) para pagar a divida, que  totalizou R${divida*(1+juros)**contador: .2f}, desses R${(divida*(1+juros)**contador)-divida: .2f} foi de juros.")
	
