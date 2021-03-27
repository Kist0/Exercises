def removeParteDiamante(linha, posicao):
    tamanho = len(linha) - 1
    linhaAux = [''] * tamanho
    for i in range(tamanho, 0, -1):
        if i != posicao:
            linhaAux[tamanho - i] = linha[i]

    tamanho = len(linhaAux)
    linha = [''] * (tamanho)
    for j in range(tamanho - 1, -1, -1):
        linha[tamanho - 1 - j] = linhaAux[j]

    return linha


def procuraDiamante():
    global linha
    global menor
    global diamante

    for j in range(0, len(linha)):
        if linha[j] == "<":
            linha = removeParteDiamante(linha, j)
            menor += 1
            return True
        elif linha[j] == ">" and menor > 0:
            linha = removeParteDiamante(linha, j)
            diamante += 1
            menor -= 1
            return True
    return False


quantidade = int(input())

for i in range(quantidade):
    linha = list(input())
    diamante = 0
    menor = 0

    while True:
        if procuraDiamante() == False:
            print(diamante)
            break