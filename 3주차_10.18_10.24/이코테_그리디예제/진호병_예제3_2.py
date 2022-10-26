n, m, k =  map(int,input().split())

arr = list(map(int,input().split()))

arr.sort(reverse=True)


firstMax = arr[0]
secondMax = arr[1]

sum = 0 

while True:
    for i in range(k):
        if m == 0 :
            break
        m -= 1
        sum += firstMax

    if m == 0 :
        break
    sum += secondMax
    m -= 1
    



print(sum)