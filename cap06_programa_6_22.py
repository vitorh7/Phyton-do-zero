# 18/03/2025
# Programa que gerencia um estoque de produtos utilizando um dicionário, onde cada item é associado a uma lista contendo a quantidade disponível e o preço unitário. Além disso, realiza operações de venda, atualizando o estoque e calculando o valor total.

# Meu objetivo com este código foi compreender como os dados são manipulados dentro de uma estrutura de dicionário e como as operações de venda impactam o estoque. Para isso, copiei um exemplo do livro para analisá-lo e adicionei comentários detalhando cada etapa.

# ==========================================

# Dicionário representando o estoque. Cada chave é o nome de um produto e seu valor é uma lista contendo:
# [0] Quantidade disponível
# [1] Preço unitário (em reais)
estoque = {
    'banana': [10, 2.99],
    'maçã': [5, 3.99],
    'laranja': [7, 1.99],
    'uva': [8, 4.99],
    'melancia': [3, 5.99],
    'morango': [6, 6.99],
    'abacaxi': [4, 7.99]
}

# Lista representando as vendas realizadas. Cada item da lista é uma sublista contendo:
# [0] Nome do produto vendido
# [1] Quantidade vendida
venda = [['banana', 2], ['maçã', 3], ['laranja', 4], ['uva', 1], ['melancia', 2], ['morango', 3], ['abacaxi', 1]]

# Variável que armazenará o valor total das vendas
total = 0

# Aqui vai percorrer a lista de vendas e realiza 2 ações importantes:
# 1. Subtrai a quantidade vendida do estoque
# 2. Calcula o valor da venda e adiciona ao total
for operação in venda:
    # Desempacota a lista operação para obter o nome do produto e a quantidade vendida
    produto, quantidade = operação

    # Obtém o preço unitário do produto a partir do dicionário estoque
    preço = estoque[produto][1]

    # Atualiza o estoque subtraindo a quantidade vendida
    estoque[produto][0] -= quantidade

    # Atualiza o valor total da venda
    total += preço * quantidade

# Exibe o total arrecadado com as vendas
print(f'Total: R$ {total:.2f}\n')

# Exibe o estoque atualizado
print('Estoque atualizado:\n')

# Percorre o dicionário estoque para exibir os produtos restantes
# O método items() retorna 