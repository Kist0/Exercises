tot, cont = 0, 0
while True:
    num = int(input('Digite um numero [999 stop]: '))
    if num == 999:
        print(f'Você digitou {cont} números e a soma deles é {tot}')
        break
    tot += num
    cont += 1