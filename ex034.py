sa = float(input('\033[1;34mQual o seu salario?\033[m'))

if sa <= 1250:
    sf = sa*15/100
    print('\033[32mSeu salario sera de R${}'.format(sf+sa))
else:
    sf = sa*10/100
    print('\033[32mO seu salario sera de R${}'.format(sf+sa))
