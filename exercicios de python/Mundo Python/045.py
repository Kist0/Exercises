from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''[0] Pedra
[1] Papel
[2] Tesoura''')
com = randint(0, 2)
mao = int(input('Qual a sua jogada? '))
print('-='*13)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO\033[1;31m')
sleep(1)
print('-='*13)
if com == 0:
    if mao == 0:
        print('-=-EMPATE-=-')
    elif mao == 1:
        print('-=-VITÓRIA!-=-')
    elif mao == 2:
        print('-=-DERROTA-=-')
    else:
        print('Jogada inválida')
elif com == 1:
    if mao == 0:
        print('-=-DERROTA-=-')
    elif mao == 1:
        print('-=-EMPATE-=-')
    elif mao == 2:
        print('-=-VITÓRIA!-=-')
    else:
        print('Jogada inválida')
elif com == 2:
    if mao == 0:
        print('-=-VITÓRIA!-=-')
    elif mao == 1:
        print('-=-DERROTA-=-')
    elif mao == 2:
        print('-=-EMPATE-=-')
    else:
        print('Jogada inválida')
print('-='*13)
print('\033[mVocê escolheu {}'.format(itens[mao]))
print('O computador escolheu {}\033[1:31m'.format(itens[com]))
