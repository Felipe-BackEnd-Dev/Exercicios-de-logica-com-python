import datetime
ano = int(input('Digite o ano de nascimento'))
atual = datetime.date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade,atual))

if idade == 18:
    print('Você tem que se alistar este ano!')
elif idade >= 19:
    saldo = idade - 18
    an = atual - saldo
    print('Você ja deveria ter se alistado em {}'.format(an))
elif idade <= 17:
    saldo = 18 - idade
    an = atual + saldo
    print('você só vai se alistar em {}'.format(an))
