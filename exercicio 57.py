sex = input("Qual seu sexo? [M/F] ").strip().upper()[0]
while sex not in "MmFf":
    print("Sexo não identificado... Digite novamente")
    sex = input("Qual seu sexo? [M/F] ").strip().upper()[0]
if sex in "fF":
    print("Você é Mulher!")
else:
    print("Você é Homem!")