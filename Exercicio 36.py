print("**BEM VINDO AO FINANCIAMENTO SIMPLES**")

valor_casa = float(input("Digite o valor da casa:  "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Quantos anos exatos você pretende pagar essa casa: ")) * 12

porcentagem_salario = salario * 30 / 100
financiamento = valor_casa / anos

"""if financiamento > porcentagem_salario:
    print("Sinto muito você não tem saldo suficiente para fazer esse financiamento")
else:
    print("Financiamento aprovado, parabens pela nova casa!")
print("-"*30)
print(f"Esse valor é 30% do seu salário: {porcentagem_salario:.2f}", end=". ")
print(f"Essas são as parcelas do financiamento: {financiamento:.2f}")
"""
# melhor financiamento
if porcentagem_salario > financiamento:
    print(f"PARABENS! SEU FINANCIAMENTO FOI APROVADO \nVALORES DAS PARCELAS: {financiamento}")
elif financiamento < porcentagem_salario:
    tentar = input("""FINANCIAMENTO NÃO APROVADO
    Para te ajudar preparamos algumas opções
    [ 1 ] """)