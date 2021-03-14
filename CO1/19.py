def computeGCD(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd
a = 12
b = 36
print("The gcd of 12 and 36 is : ", end="")
print(computeGCD(12, 36))
