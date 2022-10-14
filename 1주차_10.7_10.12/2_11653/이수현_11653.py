N = int(input())

def factorization(x):
    d = 2

    while d <= N:
        if x % d == 0:
            print(d)
            N = N / d
        else:
            d = d + 1

factorization(N)
