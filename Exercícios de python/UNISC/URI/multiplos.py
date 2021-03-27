txt = input().split()
a = float(txt[0])
b = float(txt[1])
if b % a == 0 or a == b or a % b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')