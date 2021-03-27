x = int(input())
y = int(input())
cont = 0
for i in range(y+1, x):
    if i % 2 == 1:
        cont += i
print(cont)