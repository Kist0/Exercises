try:
    txt = input().split()
    a, b, c = txt
    a = float(a)
    b = float(b)
    c = float(c)
    d = b**2 - 4*a*c
    if d<0:
        raise
    x1 = (-b + d ** 0.5) / (2*a)
    x2 = (-b - d ** 0.5) / (2*a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))
except:
    print('Impossivel calcular')