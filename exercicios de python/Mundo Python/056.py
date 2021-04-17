#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais
#velho e quantas mulheres têm menos de 20 anos.

idadeTot = 0
maiorIdade = 0
contFem = 0

for i in range(1, 5):
    print('-=-= {}° PESSOAS =-=-'.format(i))
    nome = input('NOME: ').upper()
    idade = int(input('IDADE: '))
    sexo = input('SEXO [M/F]: ').upper()

    idadeTot += idade
    idadeTot = idadeTot / 4

    if sexo == 'M':
        if idade > maiorIdade:
            maisVelhoNome = nome
            maiorIdade = idade

    if sexo == 'F':
        if idade < 20:
            contFem += 1

print('A média de idade do grupo é {:.1f} anos'.format(idadeTot))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdade, maisVelhoNome))
if contFem == 1:
    print('Há 1 mulhere com menos de 20 anos')
elif contFem > 1:
    print('Ao todo são {} mulheres com menos de 20 anos'.format(contFem))
else:
    print('Não há nenhuma mulher com menos de 20 anos')
