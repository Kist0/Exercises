class No:

  def __init__(self, v):
    self.valor = v
    self.prox = None


class listaEncadeada:

  def __init__(self):
    self.inicio = None
    
  def inserir_inicio(self, valor):
    novo = No(valor)
    No.prox = self.primeiro
    self.primeiro = novo

  def mostrar_lista(self):
    if self.primeiro != none:
      print('Lista vazia')
    else:
      while atual != none:
        print(atual.valor)
        atual = atual.prox

  #inserir no fim
  def inserir_fim(self, )