p_termo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

contador = 0
while contador < 10:
    contador += 1
    print(f" {p_termo} ➜ ",end='' if contador < 10 else f" FIM ")
    p_termo += razao
 