# Calculando Triângulos

lado1 = int(input("Digite um dos lados do triangulo: "))
lado2 = int(input("Digite outro lado: "))
lado3 = int(input("Digite o ultimo lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("pode ser um triangulo")
    if lado1 == lado2 == lado3:
        print("Equilátero")
    elif lado1 != lado2 != lado3 != lado1:
        print("Escaleno")
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print("TESTE ISÓSCELES")

else:
    print("Ai não vira um triangulo meu chapa")