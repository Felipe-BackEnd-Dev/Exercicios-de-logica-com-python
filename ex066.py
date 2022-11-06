count = soma = n1 = 0

while True:
    count = int(input('Digite um valor: '))
    if count == 999:
        break
    soma += count
    n1 += 1
print('A soma do valor é {}'.format(soma))
print('Foram digitados {} numeros'.format(n1))
