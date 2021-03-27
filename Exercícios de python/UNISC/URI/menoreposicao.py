n = int(input(''))
r = input().split()
for i in range(n):
    r[i] = int(r[i])
print('Menor valor: {}'.format(str(min(r))))
print('Posicao: {}'.format(str(r.index(min(r)))))