from datetime import date
nasc = int(input('Qual o ano do seu nascimento? '))
ano = date.today().year
idade = ano - nasc
print('Você tem {} anos e é considerado(a) um '.format(idade), end='')
if idade <= 9:
    print('nadador(a) \033[1:36mMIRIM')
elif idade <= 14:
    print('nadador(a) \033[1:36mINFANTIL')
elif idade <= 19:
    print('nadador(a) \033[1:36mJUNIOR')
elif idade <= 20:
    print('nadador(a) \033[1:36mSÊNIOR')
else:
    print('nadador(a) \033[1:36mMASTER')