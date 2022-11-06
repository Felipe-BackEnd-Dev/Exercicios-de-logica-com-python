p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
a = 1
p1 = p
while a <= 9:
    p += r
    print(p, end=' > ')
    a += 1
print('Fim')