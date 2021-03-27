num = int(input('Digite um número para ser convertido '))
print('''Escolha umas das bases para conversão
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADICMAL''')
op = int(input('Sua opção '))
if op == 1:
    print('Convertendo {} para BINÁRIO para fica {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('Convertendo {} para OCTAL para fica {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('Convertendo {} para HEXADECIMAL para fica {}'.format(num, hex(num)[2:]))
else:
    print('Digite um número válido')