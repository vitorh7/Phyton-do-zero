#Abaixo há um código que faz pesquisa e conta quantos chamados Carlos que possui ensino superior há na lista.
Lista = [("Carlos", "Médio"), ("Mariana", "Superior"), ("Carlos", "Superior"), ("Joana", "Fundamental"), ("Carlos", "Superior"), ("Mário", "Médio"), ("Carlos", "Médio"), ("Mariana", "Superior")]
#Variável que armazena quantos nomes e ensino receberam True
contagem=0
for pessoas in Lista:
#Criando variáveis para guardar valor True caso achar o nome e o ensino procurado.
    nome=False
    ensino=False
    for info in pessoas:
        if info == "Carlos":
           nome=True
        if info == "Superior":
           ensino=True
    #Verifica se foi achado as duas informações buscadas.
    if nome == True and ensino == True:
        contagem+=1
print(f"Há {contagem} Carlos com ensino superior na lista.")