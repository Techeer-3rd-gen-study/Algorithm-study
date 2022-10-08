def fun(x):
    num = 2

    while num <= x:
        if x % num == 0:
            x = x/num
            print(num)
        else :
            num += 1

n = int(input())

fun(n)
