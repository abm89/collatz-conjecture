import math

x = input("Input a number for x: ")
x = int(x)
count = 0

while (count < 100000) and (x > 1):
    if (x % 2) == 0:
        x = x // 2
        print (x)

    else:
        x = ((3 * x) + 1)
        print (x)

    count += 1