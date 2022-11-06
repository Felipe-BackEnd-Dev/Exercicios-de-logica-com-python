n1 = 0
while True:
    n1 = int(input('Você quer ver a tabuada de qual numero?'))
    if n1 <= -1:
        break
    for a in range(0, 11):
        print('{} x {:2} = {}'.format(n1, a, n1*a))
print('Programa finalizado')
