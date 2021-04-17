r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Um triângulo pode ser formado!')
    if r1 == r2 and r2 == r3 and r1 == r3: #ou r1 == r2 == r3
        print('Triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo isóceles')
    else: #r1 != r2 != r3 != r1
        print('Triângulo escaleno')
else:
    print('Um triângulo não pode ser formado')
