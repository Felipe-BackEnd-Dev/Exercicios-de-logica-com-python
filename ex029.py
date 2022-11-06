ve = int(input('Digite a velocidade do carro: '))


if ve >= 80:
    print('VOCÊ FOI MULTADO POR EXCESSO DE VELOCIDADE!')
    print('No valor de R${}'.format((ve-80)*7))
else:
    print('Pode prosseguir esta liberado, Diriga com cuidado.')