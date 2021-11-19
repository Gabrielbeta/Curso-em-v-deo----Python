# Progressão aritmética em loop
p_termo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
contador = 1
repetidor = 10
while repetidor != 0:
        
    while contador <= repetidor:
        
        contador += 1
        print(f" {p_termo} ➜ ",end='' if contador <= repetidor else f" PAUSA \n")
        p_termo += razao
    continuar = int(input("Quantos termos você quer mostrar a mais? "))
    if continuar:
        repetidor += continuar
    elif continuar == 0:
        break
print(f"Progressão finalizada com {contador - 1} temos mostrados")
