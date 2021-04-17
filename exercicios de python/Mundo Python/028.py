import random
from time import sleep
num = random.randint(0,5)
print('-=-'*8)
print('Adivinhação de número')
print('-=-'*8)
numus = int(input('Digite um número: '))
print('-=-'*8)
print('Precessando...')
sleep(2)
print('-=-'*8)
if num == numus:
    print('Você acertou!')
else:
    print('Você errou :(')
print('-=-'*8)
print('Eu escolhi {}'.format(num))
print('Você escolheu {}'.format(numus))
