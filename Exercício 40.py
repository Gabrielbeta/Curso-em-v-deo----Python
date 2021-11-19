# média do aluno

media1 = float(input("Digite a primeira nota: "))
media2 = float(input("Digite a segunda nota: "))

aluno = (media1 + media2) / 2

print("MÉDIA: {}".format(aluno))
if aluno < 5:
    print("REPROVADO")
elif aluno >= 5 <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
