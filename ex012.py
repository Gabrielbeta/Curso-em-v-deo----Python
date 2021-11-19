"""
Esse programa mede a porcentagem de desconto de um determinado item
"""

p = float(input('Qual o preço do produto? R$'))

t = float(input('Qual a porcentagem de desconto desse produto? \n(Informe apenas os números)'))

taxa = t/100
valor_desconto = p * taxa

print('Esse produto teve um desconto de {:.2f} reais'.format(valor_desconto))
total = p - valor_desconto

print('O produto inserido, com um desconto de {}% \nagora custa {:.2f} reais'.format(t, total))
