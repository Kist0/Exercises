pre = float(input('Digite o valor do produto: '))
print('------------------------\n'
      'à vista no dinheiro  (1)\n'
      'à vista no cartão    (2)\n'
      'em até 2x no cartão  (3)\n'
      '3x ou mais no cartão (4)\n'
      '------------------------')
pag = int(input('Qual a forma de pagamento? '))
if pag == 1:
    precofim = pre * 0.9
elif pag == 2:
    precofim = pre * 0.95
elif pag == 3:
    precofim = pre
elif pag == 4:
    precofim = pre * 1.2
else:
    print('Digite uma valor válido')
print('Você irá pagar {}'.format(precofim))