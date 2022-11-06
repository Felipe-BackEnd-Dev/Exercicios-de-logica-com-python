cidade = str(input('Digite o nome de um Lugar: ')).strip()
print('{} Tem a Palavra "Santo?"'.format(cidade))
print(cidade[:5].upper() == 'SANTO')
