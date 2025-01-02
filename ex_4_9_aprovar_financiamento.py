###################
# Parte do livro Introdução à Programação com Python (edição 3)
# Site: https://python.nilo.pro.br/
# Edicao 3: ex4.9 28/12/2024
###################
emprestimo=float(input("Digite o valor da casa para fazer o empréstimo: "))
salario=float(input("Qual é seu salário?: "))
tempo=float(input("Quanto tempo para pagar as parcelas da casa em anos?: "))
if emprestimo/(tempo*12)<=salario*0.3:
	print("Seu empréstimo está aprovado!")
	print(f"As parcelas custarão R${emprestimo/(tempo*12): .2f}, que estão dentro do limite de 30% do seu salário!")
else:
	print("Empréstimo reprovado! As parcelas excedem 30% do seu salário!")
