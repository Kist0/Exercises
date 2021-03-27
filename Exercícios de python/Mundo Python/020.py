from random import shuffle
a1 = input('digite o nome do primeiro aluno: ')
a2 = input('digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('digite o nome do quarto aluno: ')
list = [a1, a2, a3, a4]
shuffle(list)
print('a ordem de apresentação é: {}'.format(list))
