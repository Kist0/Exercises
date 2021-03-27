v = int(input('Qual a velocidade do carro? '))
if v >80:
    print('Você esta acima do limite de velocidade!')
    multa = float(v - 80)
    print('Você terá que pagar R${:.2f} de multa'.format(multa*7))
else:
    print("Você esta correto!")