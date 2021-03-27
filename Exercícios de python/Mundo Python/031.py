d = int(input('Qual a distância da sua viagem? '))
if d <=200:
    preco = float(d*0.5)
else:
    preco = float(d*0.45)
print('O valor da sua viagem será: {:.2f}'.format(preco))