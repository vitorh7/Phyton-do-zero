###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.15.
# data: 02/01/2025
###################
carrinho = 0
print("OLÁ!!! Venha ver o que vc pode comprar: \nBanana: código 1\nPão carioca: código 2\nArroz: código 3")
while True:
	compra = int(input("Digite o código do produto ou aperte 0 para cancelar:  "))
	if compra == 0:
		break
	elif compra!=1 and compra!=2 and compra!=3:
		print("Código inválido!")
		break
	elif compra==1:
		carrinho+=0.5
	elif compra==2:
		carrinho+=1
	elif compra==3:
		carrinho+=4
print(f"Seu carrinho deu R${carrinho}.")
		