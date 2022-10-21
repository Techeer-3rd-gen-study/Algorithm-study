A, B, C, M = map(int, input().split())

currentA = 0
totalC = 0

if A > M:
    print(0)
else:
    for i in range(24):
        if currentA <= M - A:
            currentA += A
            totalC += B
        else : 
            currentA -= C
            if currentA < 0:
                currentA = 0

    print(totalC)