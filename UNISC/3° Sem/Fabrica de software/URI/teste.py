def fib_calls(n, b, v):
    if v[(n%2)] != -1:
        return v[(n%2)]
    if (n < 2):
        return 1
    v[(n%2)] = 1 + fib_calls(n - 1, b, v) + fib_calls(n - 2, b, v)
    if (v[(n%2)] > b):
        return v[(n%2)]%b
    return v[(n%2)]
        

x = 1
n, b = input().split()
n = int(n)
b = int(b)
while n != 0 or b != 0:
    v = {-1,-1}
    print ("Case {}}: {}} {} {}".format(x, n, b, fib_calls(n, b, v)%10))
    x += 1
    n, b = input().split()
    n = int(n)
    b = int(b)