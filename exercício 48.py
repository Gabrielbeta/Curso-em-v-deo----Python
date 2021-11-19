soma = 0
quantidade = 0
for i in range(0,501,3):
    if i % 2 != 0:
        soma += i
        quantidade += 1

print(f"a soma dos {quantidade} valores é: {soma}")
