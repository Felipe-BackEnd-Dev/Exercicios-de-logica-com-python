print('-=-'*20)
print('\033[1;34mANALISADOR DE TRIÂNGULOS')
print('-=-'*20)

a = float(input('Primeiro segmento'))
b = float(input('Segundo segmento'))
c = float(input('Terceiro segmento'))
if a < b + c and b < a + c and c < a + b:
    print('\033[32mOs Segmento forma um triangulo!')
else:
    print('\033[31mO segmento não pode forma um triangulo')
