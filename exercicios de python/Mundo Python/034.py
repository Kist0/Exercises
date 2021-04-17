sal = float(input('Qual o seu salário? '))
if sal >= 1250.00:
    salaum = sal * 1.1
else:
    salaum = sal * 1.15
print('O seu salário com aumento vai de R${:.2f} para R${:.2f}'.format(sal, salaum))