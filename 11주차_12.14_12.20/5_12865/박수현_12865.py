# 도움을 받은 링크 주소입니다
# https://claude-u.tistory.com/208

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        # weight보다 작으면 위의 값을 그대로 가져옴
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] 
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])
