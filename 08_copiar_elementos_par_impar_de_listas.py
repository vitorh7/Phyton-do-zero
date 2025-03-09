#09/03/2025
# APRENDENDO A COPIAR ELEMENTOS DE LISTAS

#Cria uma lista com 100 elementos de 1 a 50
L = list(range(1, 51))
#Cria duas listas vazias
par = []
impar = []
#Percorre a lista L
for i in L:
    #Se o número for par, adiciona à lista par
    if i % 2 == 0:
        par.append(i)
        #Se não, adiciona à lista impar
    else:
        impar.append(i)
print("Pares:", par, "\nÍmpares:", impar)