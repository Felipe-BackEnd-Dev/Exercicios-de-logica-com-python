peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura'))
imc = peso/(altura*altura)
print('O seu imc é de {:.2f}Kg'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')