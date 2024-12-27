#Exercício de Lógica de Programação
#nome: Vitor Pereira
#data: 19/12/3024
#phydroid3

ano_atual= int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual-ano_nascimento
#Subtrair os anos para chegar na idade da pessoa.
verificador = idade>=18
#Verifica se idade é igual ou maior que 18
print(f"maioridade: {verificador}, tem {idade}  anos!") 