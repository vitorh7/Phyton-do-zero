#Exercício de Lógica de Programação
#nome: Vitor Pereira
#data: 19/12/3024
#phydroid3

altura = float(input("Digite sua altura em metros: "))
#pede altura do usuário (variável)
peso = float(input("Digite seu peso em Kg: "))
#pede o peso do usuário (variável)
imc = peso/altura**2
#cálculo imc (operador aritimético)
ideal = 18.5<=imc<=24.9
#define a faixa ideal do IMC (operador relacional)
print(f"Seu IMC é: {imc: .2f}, ele é ideal: {ideal}")
#as variáveis estão dentro da string, um valor numérico e um booleano
