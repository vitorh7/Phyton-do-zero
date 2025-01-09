###############################
# Código baseado no livro "Introdução à Programação com Python" (3ª edição)
# Site: https://python.nilo.pro.br/
# Edição 3: Exemplo 5.27
# Data: 08/01/2025
###############################

# Este programa verifica se um número ou uma palavra é um palíndromo.
# A verificação é feita comparando os caracteres das extremidades 
# (da esquerda para a direita e vice-versa), verificando todos os 
# caracteres até o final da string. O programa para assim que 
# encontra uma discrepância ou conclui a comparação completa.

while True:
    # Exibe o menu e solicita ao usuário uma entrada.
    x = input("Digite um número ou palavra para verificar se é um palíndromo ou digite 0 para encerrar o programa: ")

    # Verifica se o usuário deseja encerrar o programa.
    if x == "0":
        break

    # Calcula o comprimento da entrada.
    tamanho = len(x)

    # Inicializa a variável para controle do índice durante as comparações.
    a = 0 

    # Compara os caracteres enquanto os índices ainda estão dentro do tamanho da string.
    while a < tamanho:
        # Pega o caractere correspondente da esquerda para a direita.
        inicio = x[a]

        # Pega o caractere correspondente da direita para a esquerda.
        fim = x[-(a + 1)]

        # Verifica se os caracteres das extremidades são diferentes.
        if inicio != fim:
            print(f"{x} não é um palíndromo!")
            break
        # Quando o índice chegar ao final sem discrepâncias, é um palíndromo.
        elif a == (tamanho - 1):
            print(f"{x} é um palíndromo!")
            break
        
        # Incrementa o índice para continuar as comparações.
        a += 1
	
