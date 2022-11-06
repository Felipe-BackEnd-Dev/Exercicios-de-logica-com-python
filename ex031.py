vi = float(input('\033[35mQual a distancia até o destino? '))
print('Você esta prestes a começar uma viagem de {}KM'.format(vi))

if vi >= 200:
    print('\033[33mSua viagem vai custar R${:.2f}'.format(vi*0.45))
else:
    print('\033[33mSua viagem vai custar R${:.2f}'.format(vi*0.50))
