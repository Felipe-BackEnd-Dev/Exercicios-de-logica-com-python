a = int(input('\033[35mPrimeiro um valor:'))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor'))
menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('\033[31mO menor numero é {}\033[m'.format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\033[34mO maior numero é {}'.format(maior))
