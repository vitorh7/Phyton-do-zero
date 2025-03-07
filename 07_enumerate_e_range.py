# 06/03/2025
# APRENDENDO A USAR FUNÇÕES range e enumerate

# Usando range()
print("Usando range():")
for t in range(3, 33, 3):
    print(t, end=' ')
print()

L = list(range(50, 501, 50))
print("Lista gerada com range():", L)

# Usando enumerate()
L = ["maçã", "banana", "laranja"]

# Normal
print("\nUsando loop normal:")
i = 0
for x in L:
    print(f"Índice {i}, fruta {x}")
    i += 1

# Com enumerate
print("\nUsando enumerate():")
for i, x in enumerate(L):
    print(f"Índice {i}, fruta {x}")

# Enumerate gera uma tupla, o primeiro elemento é o índice e o segundo é o valor (i, x)
# Isso é possível pois Python permite desempacotamento de tuplas
# A cada execução, a função enumerate retorna (0, "maçã"), (1, "banana"), (2, "laranja")

# Trocando i, x por z para não desempacotar a tupla
print("\nUsando enumerate() sem desempacotamento:")
for z in enumerate(L):
    print(z)