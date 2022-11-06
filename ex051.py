p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for a in range(p, d+r, r):
    print('{}'.format(a), end=' > ')
print('FIM')