dias = int(input('Informe a quantidade de dias que o carro ficou alugado: '))
km = float(input('Informe a quantidade de Km rodados: '))
print('O valor do aluguel ficou: R${:.2f}'.format((dias * 60) + (km * 0.15)))
