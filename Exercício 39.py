#
# Alistamento Militar
#

from datetime import date
hoje = date.today()
ano_hoje = hoje.year

nascimento = int(input("Informe seu ano de nascimento: "))
idade = ano_hoje - nascimento

if idade > 18:
    print(f"Sua idade: {idade} Anos\nVocê se alistou a {idade - 18} Anos(s) já passou seu tempo de Alistamento")
elif idade == 18:
    print(f"Este é o momento para você se alistar")
elif idade < 18:
    print(f"Sua idade: {idade} Anos\nAinda faltam {18 - idade} Ano(s) para você se alistar")
else:
    print("Algo deu errado no programa")



