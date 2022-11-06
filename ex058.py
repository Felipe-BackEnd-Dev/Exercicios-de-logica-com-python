import random
print('Lets play a game?')
print('try to guess a number between 0 and 10')
n1 = random.randint(0, 10)
t = 0
n2 = 11
while n1 != n2:
    n2 = int(input('Try: '))
    t += 1
    if n1 > n2:
        print('Hmm é mais tente novamente')
    if n1 < n2:
        print('HMMMMM é menos')
print('Your number {}/ PC number {}'.format(n2, n1))
print('You Win, {} Try again'.format(t))
