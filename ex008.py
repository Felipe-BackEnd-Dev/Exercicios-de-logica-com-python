n1 = float(input('Digite um valor: '))
km = n1/1000
hm = n1/100
dam = n1/10
dm = n1*10
cen = n1*100
mm = n1*1000
print('{} Metros \n{:.3f}Km \n{:.2f}Hm \n{:.1f}Dam \n{:.0f}Dm \n{:.0f}Cm \n{:.0f}Mm'.format(n1, km, hm, dam, dm, cen, mm))
