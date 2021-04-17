frase2 = ''
frase = input('Digite uma frase: ').strip().upper().replace(' ', '')
print(frase)
for i in range(len(frase) - 1, -1, -1):
    frase2 += frase[i]
print(frase2)
if frase == frase2:
    print('É um palíndromo')
