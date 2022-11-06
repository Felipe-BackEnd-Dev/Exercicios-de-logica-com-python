resp = 'S'
m = 0
soma = 0
quant = 0
maior = 0
menor = 0
while resp in 'sS':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if quant == 1:
        maior = menor = num

    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
m = soma/quant
print('Acabou')
print('Você digitou {} numeros e a media é {}'.format(quant, m))
print('O menor valor foi {} e o maior foi {}'.format(menor, maior))
