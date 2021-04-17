x = int(input())
led = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for i in range(x):
    s = 0
    seq = input()
    for j in seq:
        s += led[int(j)]
    print('{} leds'.format(s))