escolha = 0

def menu():
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa \n''')

    return int(input('    O que você deseja fazer com estes números? '))

primeiroValor = int(input('Digite o primeiro valor: '))
segundoValor = int(input('Digite o segundo valor: '))

while True:
    escolha = menu()
    if escolha == 1:
        print('    A soma de {} e {} é {}'.format(primeiroValor, segundoValor, primeiroValor + segundoValor))
    if escolha == 2:
        print('    A multiplicação de {} e {} é {}'.format(primeiroValor, segundoValor, primeiroValor * segundoValor))
    if escolha == 3:
        if primeiroValor > segundoValor:
            print('    {} é maior'.format(primeiroValor))
        else:
            print(f'{segundoValor} é maior')
    if escolha == 4:
        primeiroValor = int(input('    Digite o primeiro valor: '))
        segundoValor = int(input('    Digite o segundo valor: '))
    if escolha == 5:
        break