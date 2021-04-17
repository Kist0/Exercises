r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Um triângulo pode ser formado!')
else:
    print('Um triângulo não pode ser formado')
