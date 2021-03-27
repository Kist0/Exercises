calculo = 1
fatorial = int(input('Digite um número para calcular o fatorial: '))
fat = fatorial
while True:
    print (f'{fat} x ', end='')
    calculo = calculo * fat
    fat -= 1
    if fat == 1:
        print(f'1 = {calculo}')
        break