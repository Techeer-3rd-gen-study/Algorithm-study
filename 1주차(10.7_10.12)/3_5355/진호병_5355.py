n = int(input())


for i in range(n):
    arr = list(input().split())
    num = float(arr[0])

    for j in range(1, len(arr)):
        if arr[j] == "@":
            num *= 3.00
        if arr[j] == "%":
            num += 5.00
        if arr[j] == "#":
            num -= 7.00
    print('%.2f' %num)