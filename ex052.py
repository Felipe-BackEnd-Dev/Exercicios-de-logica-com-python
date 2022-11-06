n1 = int(input('Digite um numero para saber se ele é primo'))
t = 0
for a in range(1, n1 + 1):
    if n1 % a == 0:
        print('\033[34m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(a), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n1, t))
if t == 2:
    print('Este é um numero primo')
else:
    print('Este não é um numero primo')
