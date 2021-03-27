# Define tamanho da lista
tamanhoLista = 4


# Define class Pessoa com nome e matricula
class Pessoa:
    nome = ''
    matricula = 0


# Define class Lista com uma lista da class pessoas e o número de elementos dentro dela
class Lista:
    alunos = [Pessoa()] * tamanhoLista
    numeroElementos = 0


# Função para criar uma lista vazia
def criaLista():
    lista = Lista()
    print("Ta ok, você criou uma lista!")
    return lista


# Função que recebe uma lista como parâmetro e imprime ela inteira
def imprimeLista(lista):
    print("[ ________ RELATÓRIO ________ ]")

    for i in range(lista.numeroElementos):
        print("[{}] Nome: {}".format(i, lista.alunos[i].nome), end="\t")
        print("Matricula: {}".format(lista.alunos[i].matricula))

    print("[{} elemento(s) ocupado(s) de {}]".format(lista.numeroElementos, tamanhoLista))


# Função para receber dados da class Pessoa e então retorná-los
def entradaDados():
    aluno = Pessoa()
    aluno.nome = input("Informe o nome.....: ")
    aluno.matricula = int(input("Informe a matricula: "))

    return aluno


# Função para colocar os dados inseridos no final da lista
def incluiFimLista(lista):
    if lista.numeroElementos < tamanhoLista:

        lista.alunos[lista.numeroElementos] = entradaDados()
        lista.numeroElementos += 1
        print("Sucesso na inclusão!!!")
    else:

        print("A lista ta cheia '-' ")

    return lista


# Função que imprime os dados da lista que estão no index escolhido
def consultaElementLista(lista):
    index = int(input("Informe o index.....: "))
    if index < lista.numeroElementos:
        print(lista.alunos[index].nome, lista.alunos[index].matricula)
    else:
        print("Index não existe")


# Função para colocar os dados inseridos no início da lista
def incluiInicioLista(lista):
    if lista.numeroElementos < tamanhoLista:

        listabkp = lista.alunos
        lista.alunos = [Pessoa()] * tamanhoLista
        lista.alunos[0] = entradaDados()

        for i in range(lista.numeroElementos):
            lista.alunos[i + 1] = listabkp[i]

        lista.numeroElementos += 1
        print("Tudo certo!")
    else:

        print("A lista ta cheia '-' ")

    return lista


# Função que deleta os dados da lista que estão no index escolhido
def excluiElementoLista(lista):
    index = int(input("Informe o index.....: "))

    if index < lista.numeroElementos:
        for i in range(index, lista.numeroElementos):
            lista.alunos[i] = lista.alunos[i + 1]

        lista.alunos[lista.numeroElementos] = Pessoa()
        lista.numeroElementos -= 1
        print("Tudo certo!")
    else:
        print("Index não existe")
    return lista


# Função que altera os dados da lista que estão no index escolhido
def alteraElementoLista(lista):
    index = int(input("Informe o index.....: "))

    if index < lista.numeroElementos:
        lista.alunos[index] = entradaDados()
        print("Tudo certo!")
    else:
        print("Index não existe")

    return lista


# Função para ordernar os elementos da lista com base na matrícula
def bubbleSort(lista):
    n = lista.numeroElementos

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if int(lista.alunos[j].matricula) > int(lista.alunos[j + 1].matricula):
                lista.alunos[j], lista.alunos[j + 1] = lista.alunos[j + 1], lista.alunos[j]

    return lista


# Função para excluir todos os valores a partir do index selecionado
def excluirProxElementos(lista):
    index = int(input("Informe o index.....: "))

    if index < lista.numeroElementos:
        for i in range(index, lista.numeroElementos):
            lista.alunos[i] = Pessoa()
            lista.numeroElementos -= 1

        print("Tudo certo!")
    else:
        print("Index não existe")

    return lista


# Função para imprimir o menu e receber a operação a ser realizada
def menu():
    while True:
        print()
        print("[ ____ SISTEMA ACADÊMICO ____ ]\n \
        1. Cria lista\n \
        2. Insere valor no fim da lista\n \
        3. Insere valor no inicio da lista\n \
        4. Remove um valor da lista\n \
        5. Imprime a lista\n \
        6. Imprime um valor da lista\n \
        7. Altera um valor da lista\n \
        8. Ordena os valores da lista\n \
        9. Remover os valores a partir do index\n \
        10. Sair")

        while True:
            opcaoMenu = input("Opção: ")
            if int(opcaoMenu) >= 0 and int(opcaoMenu) <= 10:
                break
        print()

        if opcaoMenu == '1':
            lista = criaLista()
        elif opcaoMenu == '2':
            lista = incluiFimLista(lista)
        elif opcaoMenu == '3':
            lista = incluiInicioLista(lista)
        elif opcaoMenu == '4':
            lista = excluiElementoLista(lista)
        elif opcaoMenu == '5':
            imprimeLista(lista)
        elif opcaoMenu == '6':
            consultaElementLista(lista)
        elif opcaoMenu == '7':
            lista = alteraElementoLista(lista)
        elif opcaoMenu == '8':
            lista = bubbleSort(lista)
        elif opcaoMenu == '9':
            lista = excluirProxElementos(lista)
        elif opcaoMenu == '10':
            print()
            print("[ ____ Valeu Falou ____ ]")
            break
        elif opcaoMenu == '0':  # EasterEgg
            print(
                '😀😃😄😁😆😅😂🤣☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😭😤😠😡🤬🤯😳🥵🥶😱😨😰😥😓🤗🤔🤭🤫🤥😶😐😑😬🙄😯😦😧😮😲🥱😴🤤😪😵🤐🥴🤢🤮🤧😷🤒🤕🤑🤠😈👿👹👺🤡💩👻💀☠️👽👾🤖🎃😺😸😹😻😼😽🙀😿😾')


# Início do programa chamando a função menu
menu()