frase = str(input('Digite sua frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('Você digitou a frase {}'.format(palavras))
for a in range(len(junto) - 1, -1, -1):
    inverso += junto[a]
print(junto, inverso)
if inverso == junto:
    print('A frase é um palindromo!')
else:
    print('A frase digitada não é um palindromo')


