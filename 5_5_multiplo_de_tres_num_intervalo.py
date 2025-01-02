#Exercício do Livro modificado
#Escrever todos os múltiplo de um número numa sequencia um intervalo.
#Ex 5.5
#01/01/2025
inicio = int(input("Digite um inicio para sequencia: "))
fim = int(input("Digite um fim para sequencia: "))
multiplo = int(input("Digite um numero para saber seus múltiplos nessa sequencia: "))
while inicio<=fim:
	if inicio%multiplo==0:
		print(inicio)
		inicio=inicio+multiplo
	else:
		inicio=inicio+1