vc = float(input('Valor da Casa: R$'))
sa = float(input('Salario: R$'))
qa = float(input('Em quantos anos vai pagar: '))
ca = vc/(12*qa)

if ca >= sa*30/100:
    print('Para pagar uma casa de {} em {} anos a prestação sera de {}'.format(vc, qa, ca))
    print('\033[31mEmprestimo NEGADO')
else:
    print('Para pagar uma casa de {} em {} anos a prestação sera de {}'.format(vc, qa, ca))
    print('\033[32mEmprestimo APROVADO')
