nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Muito prazer em te conhecer')
print('Seu Primeira nome é: {}'.format(n[0]))
print('Seu Ultimo nome é: {}'.format(n[len(n)-1]))