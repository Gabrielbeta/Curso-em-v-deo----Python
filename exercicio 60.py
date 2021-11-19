fatorial = int(input(f" {'*' * 30}FATORIAL{ '*' * 30} \nDigite um número: "))
inicial = fatorial
print(f'{inicial}! = ', end='')
for num in range((inicial-1),0,-1):
    fatorial *= num
    if inicial == 2:
        print(f'{inicial} X {num} = {fatorial}') 
        break
    print(f'{num} X ' if num > 1 else f'{num} = {fatorial}', end='')
