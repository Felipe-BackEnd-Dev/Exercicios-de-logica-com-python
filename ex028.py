import random
import time
print('-=-' * 20)
print('Tente descobrir o numero de 1 a 3 que estou pensando')
print('-=-' * 20)
num = int(input('Em qual numero pensei? '))
print('PROCESSANDO.....')
time.sleep(2)
rand = random.randint(1, 3)
if num == rand:
    print('Você venceu! o numero é {}'.format(rand))
else:
    print('Você perdeu! o numero era {}'.format(rand))
