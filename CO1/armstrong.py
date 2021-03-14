for i in range(1, 501):
    sum = 0
    num = i
    while num > 0:
        rem = num % 10
        sum = sum+rem**len(str(i))
        num = num//10
        if i == sum:
            print(i)