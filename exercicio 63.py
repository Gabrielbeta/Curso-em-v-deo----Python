
fibonacci_one = 0
fibonacci_two = 1
inicializador = 0
repetidor = int(input("Quantos números da sequência fibonacci você deseja mostrar? "))
contador = repetidor
while repetidor != 0:
    while inicializador <= contador:
        inicializador +=1
        fibonacci_three = fibonacci_two
        fibonacci_two = fibonacci_two + fibonacci_one
        fibonacci_one = fibonacci_three
        print(f"{fibonacci_two} ➜ ", end="" if inicializador <= contador else f" Pausa \n" )
                
    repetidor = int(input("Quantos números da sequência fibonacci você deseja mostrar? "))
    if repetidor:
        contador += repetidor
print("Obrigado por usar o programa!")
nome = input("Por favor informe seu nome: ")
print(f"obrigado {nome} você foi percorreu {inicializador} números da sequência (maior número: {fibonacci_two})")

"""
lista_fibonacci = []
lista_fibonacci.append(fibonacci)
lista_fibonacci.append(1)

while contador != 0:
    while inicializador <= contador:
        lista_fibonacci.append(lista_fibonacci[-1] + lista_fibonacci[-2]) 
        inicializador +=1

    print(lista_fibonacci)
    contador = int(input("Quantos números da sequência fibonacci você deseja mostrar? "))
"""



