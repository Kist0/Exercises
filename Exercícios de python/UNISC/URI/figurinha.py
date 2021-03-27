def mdc_recursivo(a, b):
    if b == 0:
        return a
    resto = a % b
    a = b
    b = resto
    return mdc_recursivo(a, b) 

qtde_casos_teste = int(input())

for i in range (qtde_casos_teste):
    x, y = input().split()
    f1 = int(x)
    f2 = int(y)
    resultado = mdc_recursivo(f1,f2)
    print(resultado)
    i += 1

# codigo de eplicação
def mdc_recursivo(a, b):
    if b == 0:
        return a
    resto = a % b
    print("{} dividido por {} = resto {} ".format(a, b, resto))
    return mdc_recursivo(b, resto) 
    
qtde_casos_teste = int(input())

for i in range (qtde_casos_teste):
    x, y = input().split()
    f1 = int(x)
    f2 = int(y)
    resultado = mdc_recursivo(f1,f2)
    print(resultado)
    i += 1