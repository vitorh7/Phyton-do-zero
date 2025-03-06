###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edição 3: ex6.11.
# Data: 06/03/2025
###################
#Modificar o programa abaixo para trocar while por for e expicar o porque de não ser possível substituir todos o for por while
###################
# L=[]
# while True:
#     n=int(input("Digite um número para adicionar na lista (0 para imprimir/sair):"))
#     if n==0:
#         break
#     L.append(n)
# x=0
# while x<len(L):
#     print(L[x])
#     x+=1
###################
#Resposta 1
L=[]
while True: #Aqui não é posível usar for pois a lista está vazia, portanto não tem um tamanho definido, chega até ser filófco, pois não tem como saber o tamanho do vazio, do que não eiste
    n=int(input("Digite um número para adicionar na lista (0 para imprimir/sair):"))
    if n==0:
        break
    L.append(n)
if not (L==[]):#Aqui é possível usar for, pois a lista possui um tamanho, que é garantido pela verificação L==[], que só é falsa se a lista não estiver vazia
    for x in L:
        print(x)
#Não coloquei verificador de tipo de dados pois o enunciado não pede, mas é uma boa prática
#Os 2 códigos acima vão dar o mesmo resultado, a diferença é que o segundo é mais elegante.

###################
#Resposta 2
#Se você deixar com dois for, ocorrerá que essa parte do programa vai se encerrar pois como a lista é criada novamente vazia, o for não é executado.
L=[]
for x in L:
    n=int(input("Digite um número para adicionar na lista (0 para imprimir/sair):"))
    if n==0:
        break
    L.append(n)
if not (L==[]):
    for x in L:
        print(x)