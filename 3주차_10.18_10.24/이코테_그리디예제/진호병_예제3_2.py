n,m = map(int ,input().split())

arr = [[0] * (m) for _ in range(n)] # arr 만들어 0으로 초기화 시킴 ex. 2 * 4

minArr = []

for i in range(n): # 만든 arr 틀에 값을 집어넣는 for 문
    lineArr = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] = lineArr[j]

for i in range(n):
    min = 10000000 # 행 별로 최소값을 주기 위해 행이 바뀔때마다 1000000으로 초기화 시켜줌 
    for j in range(m):
        if min > arr[i][j]:
            min = arr[i][j]

    minArr.append(min)

print(max(minArr))


