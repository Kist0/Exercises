s = 0
cont = 0
for i in range(0,6):
    v = int(input('Digite um valor: '))
    if v % 2 == 0:
        s += v
        cont += 1
print('A soma dos {} valores pares informados é {}'.format(cont, s))
