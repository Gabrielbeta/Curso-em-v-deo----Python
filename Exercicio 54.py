#Solicita a idade das 7 pessoas
from datetime import date

ano = date.today().year

maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input(f"Digite o ano de nascimento da {i}° pessoa: "))
    if (ano - nasc <= 21):
        menor += 1
    else:
        maior += 1

print(f"Ao todo tivemos {maior} pessoas maiores de idade")
print(f"Ao todo tivemos {menor} pessoas menores de idade")