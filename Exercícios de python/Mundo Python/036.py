val = float(input('\033[1;33mQual o valor da casa? '))
sal = float(input('\033[1;34mQual o seu salário? '))
tem = int(input('\033[1;36mEm quantos anos você irá pagar? \033[m')) * 12
parm = val / tem
if parm > sal * 0.3:
    print('\033[1;31mA parcela mensal ({:.2f})não pode exceder 30% do seu salário, -NEGADO-'.format(parm))
else:
    print('\033[1;32mVocê está -APTO- a pagar as prestações de {:.2f} da casa!\033[m'.format(parm))