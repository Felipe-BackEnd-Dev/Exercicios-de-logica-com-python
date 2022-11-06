import random
print('-=-'*15)
print('Vamos jogar Jokempo?')
print('-=-'*15)
opt = int(input('''[0] Para Tesoura
[1] Para Pedra
[2] Para Papel'''))
rand = random.randint(0, 2)

itens = ('Tesoura', 'Pedra', 'Papel' )


print('Você colocou {} e o computador colocou {}'.format(itens[opt], itens[rand]))

if opt == 0 and rand == 2:
    print('Você Venceu!')

elif opt == 1 and rand == 0:
    print('Você venceu!')

elif opt == 2 and rand == 1:
    print('Você venceu!')
elif opt == rand:
    print('EMPATOU!')
else:
    print('Você perdeu!')