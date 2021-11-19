
nome_maior = ""
maior_idade = 0
contagem = 0
soma_idade = 0
cont_mulheres = 0
for i in range(1,5):
    print(f"-----{i}° PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip()
    if sexo.upper() in "Mn" and idade > maior_idade:
        maior_idade = idade
        nome_maior = nome
    if sexo.upper() in "Ff" and idade < 20:
        cont_mulheres += 1
    contagem += 1
    soma_idade += idade
media = soma_idade / contagem

print(f"A média de idade do grupo é de {media} anos")
print(f"O homem mais velho tem {maior_idade} anos e se chama {nome_maior}.")
print(f"Ao todo são {cont_mulheres} mulher(es) com menos de 20 anos")

