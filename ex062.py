print('Gerador de PA')
print('-=-'*10)
primeiro = int(input('primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while count <= total:
        print('{}'.format(termo), end=' > ')
        termo += razão
        count += 1
    print('Pausa!')
    mais = int(input('Quantos termos você quer mostra a mais'))
print('FIM!')
print('total de progração mostradas {}'.format(total))
