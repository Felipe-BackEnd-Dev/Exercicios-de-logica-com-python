n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n2 > n1:
    print('O segundo valor é maior ({})'.format(n2))
elif n1 > n2:
    print('O primeiro valor é maior ({})'.format(n1))
else:
    print('Os dois são iguais')
