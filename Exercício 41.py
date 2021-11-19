# Categoria do nadador

from datetime import date

nasc = int(input("Digite o ano de nascimento: "))
idade = date.today().year - nasc

if idade <= 9:
    print(f"VOCÊ TEM {idade} ANOS - CATEGORIA MIRIM")
elif idade > 9 and idade <= 14:
    print(f"VOCÊ TEM {idade} ANOS - CATEGORIA INFANTIL")
elif idade > 14 and idade <= 19:
    print(f"VOCÊ TEM {idade} ANOS - CATEGORIA JÚNIOR")
elif idade > 19 and idade <= 25:
    print(f"VOCÊ TEM {idade} ANOS - CATEGORIA SÊNIOR")
elif idade > 25:
    print(f"VOCÊ TEM {idade} ANOS - CATEGORIA MASTER")

