width = float(input('Qual a largura da parede?'))
height = float(input('Qual a altura da parede?'))
repaint = int(input('Quantas vezes tem que repassar a tinta? '))
ar = width*height
re = ar*repaint
bucks = re/2
print('Largura: {} \nAltura: {} \nDemão: {}'.format(width, height, repaint))
print('{} x {} = {}'.format(width, height, ar))
print('{} x {} = {}'.format(ar, repaint, re))
print('{} / {} = {}'.format(re, 2, bucks))
print('serão necessarias {} litros de tintas'.format(bucks))
