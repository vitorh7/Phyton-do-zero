#18/03/2025
#Programa com dicionário que contém listas, representando estoque e preço de produtos, além de operação de vendas.
#Meu objetivo aqui foi entender como os dados são ediatos num dicionário e como as operações são realizadas, por isso copiei o exemplo do livro e comentei o que cade linha faz
#==========================================
#Aqui temos um dicionário com produtos e suas respectivas quantidades e preços
estoque = {
    'banana': [10, 2.99],
    'maçã': [5, 3.99],
    'laranja': [7, 1.99],
    'uva': [8, 4.99],
    'melancia': [3, 5.99],
    'morango': [6, 6.99],
    'abacaxi': [4, 7.99]}
#Cria uma lista de lista para armazenar os produtos vendidos, onde uma lista interna contém o nome do produto e a quantidade vendida
venda = [['banana', 2], ['maçã', 3], ['laranja', 4], ['uva', 1], ['melancia', 2], ['morango', 3], ['abacaxi', 1]]
#Cria uma variável para armazenar o valor total da venda
total = 0
#A lista venda será percorrida com for para cada venda, e realizar 2 ações:
#1. Subtrair a quantidade vedida no dicionário de estoque.
#2. Somar ao total o valor da venda.
for operação in venda:
#Como vendas é uma lista de listas é preciso desempacotar os valores:
    produto, quantidade = operação
#Aqui pegamos o preço do produto no dicionário estoque
    preço = estoque[produto][1]
#Aqui subtraímos a quantidade vendida do dicionário estoque
    estoque[produto][0] -= quantidade
#Aqui somamos ao total o valor da venda
    total += preço * quantidade
print(f'Total: {total:.2f}\n')
print('Estoque:\n')
#Aqui percorremos o dicionário estoque. O método items() retorna uma tupla (chave, valor),
#onde a chave é o nome do produto e o valor é a lista com quantidade e preço.
#O for desempacota a tupla em duas variáveis: produto e dados.
for produto, dados in estoque.items():
    #Aqui desempacotamos a lista dados em duas variáveis: quantidade e preço.
    quantidade, preço = dados
    #Por fim, imprimimos o produto, a quantidade e o preço
    print(f'{produto}: {quantidade} unidades, R$ {preço:.2f} cada')