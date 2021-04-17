peso = 0

for i in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa '.format(i)))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}'.format(maior))
print('O menor peso lido foi {}'.format(menor))
