m = float(input('Digite um valor em metros: '))
while m != 0:
    print('Você digitou o número {} em metros\nVeja ele nas demais medidas:'.format(m))
    print((m/1000), 'Km')
    print((m/100), 'hm')
    print((m/10), 'dam')
    print((m*10), 'dm')
    print((m*100), 'cm')
    print((m*1000),'mm')
    m = float(input('Digite um valor em metros: '))
else:
    print('Você digitou 0')
    input('Pressione <Enter> para sair')

 
