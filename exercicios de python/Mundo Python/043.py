altura = float(input('Qual a sua altura?(m) '))
peso = float(input('Qual o seu peso?(kg) '))
imc = peso / altura**2
print('Seu IMC é {:.1f}\033[1:36m'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')