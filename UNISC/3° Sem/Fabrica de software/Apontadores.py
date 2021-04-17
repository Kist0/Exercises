#alocacaog dinamica
import osA

class No:
    
    def __init__(self,v):
        self.valor = v
        self.prox = None #nao aponta

class ListaEncadeada:
    
    def __init__(self):
        self.primeiro = None #nao aponta

    def inserir_inicio(self,valor):
        novo = No(valor)
        novo.prox = self.primeiro
        self.primeiro = novo

    def imprimir(self):
        if self.primeiro == None:
            print('Lista Vazia')
        else:
            atual = self.primeiro
            while atual != None:
                print('[',atual.valor,']')
                atual = atual.prox #caminhamento

    def inserir_fim(self,valor):
        novo = No(valor)
        if self.primeiro == None: #se a lista eh vazia, o processo eh o mesmo de inserir no inicio
            self.primeiro = novo
        else:
            atual = self.primeiro
            while atual.prox != None: #senao, percorre-se a lista ate chegar ao final
                atual = atual.prox    #e fazemos o ultimo elemento apontar para nodo em vez de para Null
            atual.prox  = novo

    def pesquisar(self,valor):
        if self.primeiro == None:
            print('Lista Vazia!')
        else:
            posicao = 0                                         #firula para imprimir 
            atual = self.primeiro
            while atual.prox != None and atual.valor != valor:  #loopa a lista ate achar valor procurado OU chegar ao final
                atual = atual.prox
                posicao += 1                                    
            if atual.valor == valor:
                print(f'Valor:[{valor}] - Posicao na lista:[{posicao}]')
            else:
                print('Valor nao encontrado na lista!')

    def ordenar(self): #bubble sort, ordena CRESCENTE
        if self.primeiro == None:
            print('Lista Vazia!')
        else:
     
       x = self.primeiro
            while x != None: #x percorre a lista 1 so vez
                y = x.prox
                while y != None: #y percorre a lista toda vez que x se move
                    if y.valor < x.valor: #se y for menor que x, trocam de valor
                        x.valor, y.valor = y.valor, x.valor
                    y = y.prox
                x = x.prox
            print('Lista Ordenada com sucesso!')

    def excluir(self,valor):
        if self.primeiro == None:
            print('Lista Vazia!')
        else:                            
            atual = self.primeiro
            anterior = atual                #nodo anterior andara sempre uma posicao atras para auxiliar na exclusao posteriormente
            while atual.prox != None and atual.valor != valor: #percorre a lista ate achar nodo buscado ou chegar ao fim
                anterior = atual                              #lembrando que o anterior sempre estara uma posicao atras
                atual = atual.prox                
            if atual.valor != valor: #se ao fim do loop o valor do atual NAO FOR o procurado, ele nao existia na lista.
                print('Valor nao encontrado na lista!')
            else:
                if atual == anterior:
                    self.primeiro = atual.prox
                else:
                    anterior.prox = atual.prox #se foi encontrado, o nodo ANTERIOR a ele agora aponta ao nodo que vem APOS ele. (pulando ele na ordem)
                atual.prox = None #ponteiro do nodo excluido aponta para None
                del atual
                print('Valor excluido com sucesso!')

opcao = int(0)
lista = ListaEncadeada()
while(opcao != 7):
    print("1 - Inserir elemento no inicio")
    print("2 - Inserir elemento no fim")
    print("3 - pesquisar elemento")
    print("4 - excluir elemento")
    print("5 - ordenar lista")
    print("6 - imprimir lista")
    print("7 - sair")
    opcao = int(input("Digite a opção desejada: "))
    if (opcao == 1):
        x = int(input("Digite o elemento desejado: "))
        lista.inserir_inicio(x)
    elif (opcao == 2):
        x = int(input("Digite o elemento desejado: "))
        lista.inserir_fim(x)
    elif (opcao == 3):
        x = int(input("Digite o elemento desejado: "))
        lista.pesquisar(x)
        input("Pressione <enter> para continuar")
    elif (opcao == 4):
        x = int(input("Digite o elemento desejado: "))
        lista.excluir(x)
        input("Pressione <enter> para continuar")
    elif (opcao == 5):
        lista.ordenar()
        input("Pressione <enter> para continuar")
    elif (opcao == 6):
        lista.imprimir()
        input("Pressione <enter> para continuar")
print(' /\/\             /\/\ ')
print("(=´T´) Até mais! (`T`=)")