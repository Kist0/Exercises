from datetime import date
maior = 0
menor = 0
anoAtual = date.today().year

for i in range(1, 8):
    ano = int(input('em que ano a {}° pessoa nasceu? '.format(i)))
    if anoAtual - ano > 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maior de idade'.format(maior))
print('E também tivemos {} pessoas menor de idade'.format(menor))
