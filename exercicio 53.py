frase = str(input("Digite a frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print(f"A frase {junto} ao contrário {inverso} é um palíndromo")
else:
    print(f"A frase \033[33m{junto}\033[m ao contrário {inverso} não é um palíndromo")