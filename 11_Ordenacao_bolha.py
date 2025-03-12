#12/03/2025
# Ordenação pelo método da bolha
L = []
while True:
    try:
        n = int(input("Digite um número inteiro (0 para terminar): "))
        if n != 0:
            L.append(n)
        else:
            break
    except:
        print('Digite um número inteiro')
fim = len(L)
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)
