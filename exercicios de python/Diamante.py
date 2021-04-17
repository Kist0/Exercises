linhas = int(input())

for j in range(linhas):
    codigo = input()
    diamante = 0
    menorQ = 0
    for i in range(len(codigo)):
        if codigo[i] == '<':
            menorQ += 1
        if codigo[i] == '>' and menorQ > 0:
            diamante += 1
            menorQ -= 1

    print(diamante)
