lista = [3]
maior = 0
menor = 0
fora = 0
for i in range (len(lista)):
    print(i)
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
for j in range (menor, maior +1):
    if j not in lista:
        fora += 1
print(maior)
print(menor)
print(fora)

#for i in range(len(lista)):
#    print(lista[i])