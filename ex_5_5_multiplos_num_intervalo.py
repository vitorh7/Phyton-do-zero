###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex5.5 30/12/2024
###################
inicio = int(input("Digite um inicio para sequencia: "))
fim = int(input("Digite um fim para sequencia: "))
multiplo = int(input("Digite um numero para saber seus múltiplos nessa sequencia: "))
while inicio<=fim:
	if inicio%multiplo==0:
		print(inicio)
		inicio=inicio+multiplo
	else:
		inicio=inicio+1
