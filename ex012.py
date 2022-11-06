v = float(input('Digite o valor do produto: R$'))
d = int(input('Agora digite o desconto: '))
vd = v*(d/100)
vf = v-vd
print('R${:.2f} x {}/100 = R${:.2f}'.format(v, d, vd))
print('R${:.2f} - R${} = R${:.2f}'.format(v, vd, vf))
print('O Valor do produto com desconto é: R${:.2f}'.format(vf))


#v - valor
#d - desconto
#vd - valor descontado
#vf - valor final