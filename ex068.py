import random
v = 0
while True:
    jogador = int(input('Digite um valor '))
    computador = random.randint(0, 11)
    total = jogador + computador
    tipo = str(input('Par ou impar?')).upper()
    while tipo not in 'IP':
        tipo = str(input('Par ou impar [P/I]')).strip().upper()
    print(f'Você jogou {jogador} e o computador {computador}')
    print(f'Total {total}')
    print('DEU PAR' if total%2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total%2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total%2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar de novo....')
print('GAME OVER!!! Você venceu {} vezes'.format(v))
