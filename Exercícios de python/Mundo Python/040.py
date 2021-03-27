n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1+n2)/2
if m >= 7:
    print('\033[1;32m-APROVADO-')
elif 5 <= m < 7:
    print('\033[1;33m-RECUPERAÇÃO-')
else:
    print(('\033[1;31m-REPROVADO-'))