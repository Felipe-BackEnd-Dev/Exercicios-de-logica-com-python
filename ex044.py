va = float(input('Valor do produto: R$'))
metodo = float(input('''Digite 1 para pagar a vista no dinheiro
Digite 2 para pagar a vista no cartão
digite 3 para pagar 2x no cartão
Digite 4 para pagar 3x ou mais no cartão'''))

if metodo == 1:
    vf = va*10/100
    print('O produto ficara no valor de {}'.format(va - vf))
elif metodo == 2:
    vf = va*5/100
    print('O produto ficara no valor de {}'.format(va - vf))
elif metodo == 3:
    print('Caso você queira dividir em duas vezes as parcela ficara no valor de {}'.format(va/2))
elif metodo == 4:
    vf = va*20/100
    print('Se você dividir em 3x ou mais as parcelas com 20% de juros ficara de {}'.format(va + vf))
else:
    print('\033[31mOpção invalida')