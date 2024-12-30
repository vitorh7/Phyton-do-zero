#O empréstimo segue a regra que a prestação não ultrapasse 30% do salário.
emprestimo=float(input("Digite o valor da casa para fazer o empréstimo: "))
salario=float(input("Qual é seu salário?: "))
tempo=float(input("Quanto tempo para pagar as parcelas da casa em anos?: "))
if emprestimo/(tempo*12)<=salario*0.3:
	print("Seu empréstimo está aprovado!")
	print(f"As parcelas custarão R${emprestimo/(tempo*12): .2f}, que estão dentro do limite de 30% do seu salário!")
else:
	print("Empréstimo reprovado! As parcelas excedem 30% do seu salário!")
