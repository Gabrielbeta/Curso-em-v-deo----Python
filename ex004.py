a = input('Digite algo: ')
print('O tipo primitivo de {} é:'.format(a),type(a))
print('{} só tem espaços?'.format(a), a.isspace())
print('{} é um número?'.format(a),a.isnumeric())
print('{} é alfabético?'.format(a),a.isalpha())
print('{} é alfanumérico?'.format(a),a.isalnum())
print('{} está em maiúculas?'.format(a),a.isupper())
print('{} está em minúsculas?'.format(a),a.islower())
print('{} está capitalizada? (a primeira letra é maiúscula?)'.format (a),a.istitle())
