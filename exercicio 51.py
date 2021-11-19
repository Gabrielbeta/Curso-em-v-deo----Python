# Entrada de termos
num =  int(input("Digite o primeiro termo da PA: "))
raz = int(input("Didite a razão: "))

# Mostrando os 10 primeitos números da PA:
print("Os 10 primeiros números são: ")
for i in range (num, ( num + (raz * 10)), raz):
    print(f"➜  {i} ",end="")
