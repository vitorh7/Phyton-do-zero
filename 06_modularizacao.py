#Formas de importar bibliotecas
#1
import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print(f"A raiz do número {num} é {math.ceil(raiz)}")
#2
from math import sqrt, ceil
num = int(input("Digite um número: "))
raiz = sqrt(num)
print(f"A raiz do número {num} é {ceil(raiz)}")