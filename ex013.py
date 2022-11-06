s = float(input('Digite seu salario: R$'))
p = float(input('Digite sua promoção: '))
sp = s*(p/100)
sf = s+sp
print('{} x {} = {:.2f}'.format(s, p, sp))
print('{} x {:.2f} = {:.2f}'.format(s, sp, sf))
print('O seu salario com promoção fica R${:.2f}'.format(sf))
