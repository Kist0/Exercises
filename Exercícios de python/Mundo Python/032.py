'''ano = int(input('Digite um ano: '))
anob = ano/4
if anob%1 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')'''

from datetime import date
ano = int(input('Digite um ano ("0" para o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))