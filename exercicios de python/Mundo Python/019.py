from random import choice
a1 = input('digite o nome do primeiro aluno: ')
a2 = input('digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('digite o nome do quarto aluno: ')
list = [a1, a2, a3, a4]
esc = choice(list)
print('o aluno escolhido foi {}'.format(esc))
