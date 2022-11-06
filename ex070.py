produto = ''
preco = 0
opt = ''
soma = 0
mais = ''
menor = 0
nome = 0
a = 0
while True:
    produto = str(input('O que quer comprar? '))
    preco = float(input('Qual o preço? '))
    nome += 1
    soma += preco
    if preco >= 999:
        a += 1
    if nome == 1 or preco < menor:
        menor = preco
        mais = produto
    opt = str(input('Digite [C] se quer continuar, ou [N] para parar')).upper()
    while opt not in 'CN':
        opt = str(input('Digite [C] se quer continuar, ou [N] para parar')).upper()
    if opt in 'Nn':
        break
print('Programa Finalizando')
print('O total foi {}'.format(soma))
print('O produto mais barato foi {} R${:.2f}'.format(mais, menor))
print('{} produtos tem o valor maior que 1000'.format(a))
