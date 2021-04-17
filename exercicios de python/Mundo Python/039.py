from datetime import date
nasc = int(input('Qual o ano do seu nascimento? '))
ano = date.today().year
idade = ano - nasc
if ano - nasc == 18:
    print('É hora de se alistar')
elif ano - nasc > 18:
    idade = idade - 18
    if idade > 1:
        print('Você se alistou à {} anos'.format(idade))
    else:
        print('Você se alistou à 1 ano')
else:
    idade = 18 - idade
    if idade > 1:
        print('Você ainda irá se alistar daqui \033[1;31m{}\033[m anos'.format(idade))
    else:
        print('Você ainda irá se alistar daqui \033[1;31m1\033[m ano')
