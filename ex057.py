m = 0
f = 0
p = 0
while p < 10:
    pe = str(input('Digite seu Sexo [M/F]')).lower()
    p += 1
    if pe == 'm':
        m += 1
    if pe == 'f':
        f += 1
    else:
        p -= 1
        print('Invalido!')
print('A dez pessoas foram cadastradas')
print('O numero de homens foram {}'.format(m))
print('O numero de mulheres foram {}'.format(f))
