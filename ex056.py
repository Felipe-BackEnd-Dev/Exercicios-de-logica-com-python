somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher = 0

for p in range(1, 5):
    print('------ {}ª Pessoa-----'.format(p))
    nome = str(input('Qual seu nome? ')).strip()
    idade = int(input('Quantos anos você tem? '))
    sexo = str(input('Sexo [M/F]'))
    somaidade += idade
    if p == 1 and sexo in 'mM':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1



mediaidade = somaidade/4
print('A media de idade é {} anos'.format(mediaidade))
print('O homem mais velho é o {} e tem {} Anos'.format(nomevelho, maioridade))
print('Tem {} mulheres com menos de 20 anos'.format(totmulher))
