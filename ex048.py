s = 0
c = 0
for a in range(1, 501, 2):
    if a % 3 == 0:
        s = s + a
        c = c + 1
        print(a, end=' ')

print('\nA soma de todos os valores é {}'.format(s))
print('Quantos numero foram usados? {}'.format(c))
