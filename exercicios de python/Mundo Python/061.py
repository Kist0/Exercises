term = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = term + (10 - 1) * razao
print (f'{term} ', end='')
calc = term
while True:
    calc = calc + razao
    print (f'{calc} ', end='')
    if calc == decimo:
        print ('FiM')
        break