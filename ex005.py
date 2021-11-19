a = int(input('Digite um número: '))
s = a+1
b = a-1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(a, b, s))

#essa forma de cima é uma boa forma se você for usar mais de uma vez
#caso queira guardar em uma variável e economizar memória é assim:

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(a, (a-1), (a+1)))
