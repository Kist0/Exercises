dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos kms rodados? '))
preco = (dias*60)+(km*0.15)
print('O total a pagar é R${:.2f}'.format(preco))