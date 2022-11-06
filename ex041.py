import datetime
atual = datetime.date.today().year
ano = int(input('Em qual ano você nasceu?'))
idade = atual - ano

print('Você tem {} anos'.format(idade))

if idade <= 9:
    print('Você é um atleta MIRIM!')
elif idade >= 9 and idade <= 14:
    print('Você é um atleta INFATIL!')
elif idade >=15 and idade <=19:
    print('Você é um atleta JUNIOR!')
elif idade >= 19 and idade <=25:
    print('Você é um atleta SENIOR')
else:
    print('Você é um atleta MASTER!')
