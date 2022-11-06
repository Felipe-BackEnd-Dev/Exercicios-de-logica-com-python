n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
me = (n1 + n2)/2
print('Sua media é {}'.format(me))

if me >= 7:
    print('\033[32mVocê foi aprovado!')
elif me >= 5 and me <= 7:
    print('\033[36mVocê esta de recuperação!')
elif me <= 5:
    print('\033[31mVocê foi reprovado!')
