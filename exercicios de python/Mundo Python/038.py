a = int(input('\033[;36mDigite um valor: '))
b = int(input('Digite outro valor: '))
if a > b:
    print('\033[1;34mO primeiro valor é maior')
elif b > a:
    print('\033[1;34mO segundo valor é maior')
else:
    print('\033[1;34mOs dois valores são iguais')