from random import randint
from time import sleep
tentativa = 1

print('-=-'*8)
print('Adivinhação de número')
print('-=-'*8)

num = randint(0, 10)
numUsuario = int(input('Digite um número: '))

print('-=-'*8)
print('Precessando...')
sleep(1)
print('-=-'*8)

if numUsuario == num:
    print('Você acertou de primeira!')
else:
    while numUsuario != num:
        if numUsuario > num:
            numUsuario = int(input('Muito alto... tente mais uma vez: '))
            tentativa += 1
        elif numUsuario < num:
            numUsuario = int(input('Muito baixo... Tente mais uma vez: '))
            tentativa += 1
    print('\n\nVocê acertou na {} tentativa'.format(tentativa))

print('Eu escolhi {}'.format(num))
print('Você escolheu {}'.format(numUsuario))
