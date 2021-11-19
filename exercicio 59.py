#sistema de menu
from time import sleep

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))

menu = 0
while menu != 5:
    print("""
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Qual o maior número?
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    """)
    try:
        menu = int(input("Qual é a sua opção? "))
        sleep(1)
        if menu == 1:
            print(f"A soma de {num1} e {num2} é: {num1 + num2}")
            print("=" * 20)
            sleep(1)

        elif menu == 2:
            print(f"A multiplicação de {num1} e {num2} é: {num1 * num2}")
            print("=" * 20)
            sleep(1)
        
        elif menu == 3:
            if num1 > num2:
                print(f"O número {num1} é maior")
            elif num1 == num2:
                print("Os números são iguais")
            else:
                print(f"O número {num2} é maior")
            print("=" * 20)
            sleep(1)
        
        elif menu == 4:
            num1 = int(input("Primeiro valor: "))
            num2 = int(input("Sgundo valor: "))
            print("=" * 20)
            sleep(1)
            
        elif menu == 5:
            print("Obrigado por participar!")

        else:
            print("Opção inválida por gentileza digite novamente")
            print("=" * 20)

        
    except:
        print("Opção inválida por gentileza digite novamente")
        print("=" * 20)
        sleep(1)
