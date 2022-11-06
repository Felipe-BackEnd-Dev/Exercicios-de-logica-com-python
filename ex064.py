a = 0
b = 0
c = False
while c != True:
    opt = int(input('Digite um valor [caso queira encerrar o programa digite "999"]'))
    a += opt
    b += 1
    if opt == 999:
        b -= 1
        a -= 999
        c = True
print('Vc digitou {} numeros, e a soma de todos é {}'.format(b, a))
