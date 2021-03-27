'''nome = input('Digite seu nome: ').lower().strip()
print('Seu nome possui Silva? {}'.format(nome[1:] == 'silva'))'''

nome = input('Digite seu nome: ').lower().strip()
print('Seu nome possui Silva? {}'.format('silva' in nome))
