print("Comparando 2 números")
pnum = float(input("Digite o primeiro número: "))
snum = float(input("Digite o segundo número: "))

if pnum > snum:
    print(f"{pnum} é maior que {snum}")
elif pnum == snum:
    print("os números são iguais")
elif pnum < snum:
    print(f"{pnum} é menor que {snum}")
else:
    print("Inconsistência no resultado")