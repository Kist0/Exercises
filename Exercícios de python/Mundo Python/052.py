n = int(input('Digite um número: '))
tot = 0
for i in range(1, n+1):
    print(i, end=' ')
    if n % i == 0:
        tot += 1
print('\nO número {} foi dividido {} vezes'.format(n, tot), end='')
if tot == 2:
    print(', portanto é um número PRIMO')
