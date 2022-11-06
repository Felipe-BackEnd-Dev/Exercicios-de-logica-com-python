sexo = ''
idade = 0
opt = ''
m = 0
f = 0
maior = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Qual o sexo? [M/F]: ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo? [M/F]: ')).upper()
    if sexo in 'mM':
        m += 1
    if idade <= 20 and sexo in 'fF':
        f += 1
    if idade >= 18:
        maior += 1
    opt = str(input('quer continuar? [S/N]: ')).upper()
    while opt not in 'SN':
        opt = str(input('quer continuar? [S/N]: ')).upper()
    if opt == 'N':
        break

print('Programa finalizando')
print('Foram cadastrados {} pessoas maiores de idade'.format(maior))
print('{} das pessoas cadastradas são homens'.format(m))
print('{} são mulheres com menos de 20 anos '.format(f))
