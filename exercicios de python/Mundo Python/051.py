term = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = term + (10 - 1) * razao
for i in range(term, decimo, razao):
    print(i)
