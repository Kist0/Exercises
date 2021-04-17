while True:
    nums = input().split()
    x = int(nums[0])
    y = int(nums[1])
    if x < y:
        print('Crescente')
    if x > y:
        print('Decrescente')
    if x == y:
        break