import time
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero : '))
opt = 0
while opt != 5:
    opt = int(input('''Ola tudo bem? O que gostaria de fazer? 
    [1] Somar
    [2] multiplicar
    [3] Ver quem é o maior
    [4] trocar de numero
    [5] Sair do programa'''))

    if opt == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif opt == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif opt == 3:
        n1 > n2
        if n2 > n1:
            print('O maior numero é {}'.format(n2))
        else:
            print('O maior numero é {}'.format(n1))
    elif opt == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero : '))

print('Programa encerrando')
for a in range(0, 5):
    time.sleep(0.5)
    print('.',  end=' ')
print('\nPrograma Finalizado, tenha um otimo dia')