n1 = int(input('Digite um valor: '))
c = n1
f = 1
while c > 0:
    print('{}'.format(c), end=' x ')
    f *= c
    c -= 1
print('\no fatorial de {} é {}'.format(n1, f))
