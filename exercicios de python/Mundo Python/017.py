'''from math import pow, sqrt, ceil
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = sqrt((pow(ca,2)+pow(co,2)))
print('A hipotenusa vale {:.2f}'.format(hip))'''

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co,ca)
print('A hipotenusa vale {:.2f}'.format(hip))