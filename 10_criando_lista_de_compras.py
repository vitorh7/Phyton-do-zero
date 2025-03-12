# 12/03/2025
# Programa que cria uma lista de compras com nome, quantidade e valor do produto

# Criando uma lista vazia para armazenar os itens da compra
Lista_de_compras = []

# Loop infinito para coletar os dados dos produtos
while True:
    produto = input("Digite o nome do produto: ")  # Solicita o nome do produto
    if produto == "fim":  # Se o usuário digitar "fim", encerra o loop
        break
    else:
        quantidade = int(input("Digite a quantidade do produto: "))  # Solicita a quantidade
        valor = float(input("Digite o valor do produto: "))  # Solicita o valor unitário do produto
        Lista_de_compras.append([produto, quantidade, valor])  # Adiciona os dados à lista

# Inicializa a variável que armazenará o valor total da compra
total = 0.0

# Exibe a lista de compras formatada
print("Compra:")
for i in Lista_de_compras:
    print(f"Produto: {i[0]:20s} | Quantidade: {i[1]:5d} | Valor: R${i[2]:.2f}")  
    total += i[1] * i[2]  # Calcula o valor total multiplicando quantidade pelo valor unitário

# Exibe o valor total da compra
print(f"Total: R${total:.2f}")
