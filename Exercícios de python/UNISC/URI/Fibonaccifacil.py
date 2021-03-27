def fibb(index, x, n, resposta, antes, aantes):
    if index < n:
        resposta = resposta + str(x) + ' '
        aantes = antes
        antes = x

        if x == 0:
            x = 1
        else:
            x = antes+aantes

        index += 1
        fibb(index, x, n, resposta, antes, aantes)
    else: 
        print(resposta[:-1])

n = int(input())
fibb(0, 0, n, '', 0, 0)

def fibb(indice, ultimo, n, resposta, penultimo, antepenultimo):
    if indice < n:
        resposta = resposta + str(ultimo) + ' '
        antepenultimo = penultimo
        penultimo = ultimo

        if ultimo == 0:
            ultimo = 1
        else:
            ultimo = penultimo+antepenultimo

        indice += 1
        fibb(indice, ultimo, n, resposta, penultimo, antepenultimo)
    else: 
        print(resposta[:-1])

n = int(input()) 
fibb(0, 0, n, '', 0, 0)