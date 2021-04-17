term = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = term + (10) * razao
calc = term
cont = 0
while True:
    print (f'{calc} ', end='')
    cont += 1
    calc = calc + razao
    if calc == decimo:
        print ('Pausa ')
        qtd = int(input('Quantos termos a mais? '))
        decimo = calc + (qtd) * razao
        if qtd == 0:
            print (f'Foram mostrados {cont} termos')
            break