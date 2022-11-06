import datetime
ano = int(input('\033[33mQual ano que você quer analisar? Digite 0 para analisar o atual: '))
if ano == 0:
    ano = datetime.date.today().year


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[32mO ano {} é um ano bissexto!'.format(ano))
else:
    print('\033[31mO ano {} não é bissexto'.format(ano))
