T = int(input())

for _ in range(T):
    mars = input().split()
    answer = 0
    for i in range(len(mars)):
        if i == 0:
            answer = answer + float(mars[i])
        else:
            if mars[i] == '@':
                answer = answer * 3
            elif mars[i] == '%':
                answer = answer + 5
            elif mars[i] == '#':
                answer = answer - 7
    print("{:.2f}".format(answer))