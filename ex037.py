import math
num =int(input('Digite um numero: '))
opt = int(input('Digite 1 Para Transformar em binario \nDigite 2 para octal \nDigite 3 para hexadecimal'))

if opt == 1:
    print('{} Convertido para binario {}'.format(num, bin(num)[2:]))
elif opt == 2:
    print('{} convertido para octal {}'.format(num, oct(num)[2:]))
elif opt == 3:
    print('{} Convertido para hexa {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida')
