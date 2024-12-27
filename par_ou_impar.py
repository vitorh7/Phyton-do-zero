#Exercício de Lógica de Programação
#nome: Vitor Pereira
#data: 24/12/3024
#phydroid3

numero = int(input("Digite um número para ver se é par ou ímpar: ")) #Entrada de dados
calculo = numero%2 #Resto da divisão por 2
verificador = calculo==0 #Se houver resto, não é par, logo a igualdade será falsa.
print(f"O número que tu digitou é par: {verificador}") #Saída de dados