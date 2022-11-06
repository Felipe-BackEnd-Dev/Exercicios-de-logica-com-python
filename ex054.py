import datetime
atual = datetime.date.today().year
totma = 0
totme = 0
for a in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu'.format(a)))
    idade = atual - ano
    if idade >= 21:
        print('Essa Pessoa é de maior')
        totma += 1
    else:
        totme += 1
        print('Essa pessoa é de menor')

print('Tivemos {} pessoas maiores e {} Pessoas menores'.format(totma, totme))
