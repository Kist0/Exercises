def fibb(num_calls):
    global count
    count += 1
    if num_calls < 2:
        return num_calls
    else:
        return fibb(num_calls-1)+fibb(num_calls-2)

casos = int(input())
for i in range(casos):
    num_calls = int(input())
    count = 0
    result = fibb(num_calls)
    print('fib({}) = {} calls = {}'.format(num_calls, count-1, result))