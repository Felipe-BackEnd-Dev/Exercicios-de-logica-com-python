nome = input('Digite seu nome: ').strip()

print('Analisando...........')
print(nome.upper())
print(nome.lower())
print('Seu Nome tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

