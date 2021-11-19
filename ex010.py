#esse exercício mede a cotação do dolar

real = float(input('Quanto dinheiro você tem na carteira? R$'))
taxa = float(input('Insira a taxa (Ou então diga < 0 > para usar a taxa do dia 17/09/2019): '))

if taxa != 0:
    dolar = real / taxa
    print('Você consegue comprar: US${}'.format(dolar)

else:
    taxaa = 4.08
    dolarr = real / taxaa
    print('Como você não inseriu taxa, a taxa usa é {} e você consegue comprar: US$'.format(taxaa, dolarr))
    
                   
