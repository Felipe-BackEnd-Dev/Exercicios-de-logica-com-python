import math
ang = float(input('Digite o angulo'))
sen = math.sin(math.radians(ang))
con = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O Seno de {} é {:.2f}'.format(ang, sen))
print('O Conseno de {} é {:.2f}'.format(ang, con))
print('A Tangente de {} é {:.2f}'.format(ang, tan))

