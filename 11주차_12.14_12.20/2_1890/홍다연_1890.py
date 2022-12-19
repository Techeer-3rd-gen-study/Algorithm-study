# 1890번 : 점프 

import sys
input = sys.stdin.readline

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if board[i][j] != 0 and dp[i][j] != 0: 
            if i + board[i][j] < n:    # 아래
                dp[i + board[i][j]][j] += dp[i][j]

            if j + board[i][j] < n:    # 오른쪽
                dp[i][j + board[i][j]] += dp[i][j]

print(dp[-1][-1]) 

# 리스트에서 -1은 마지막 요소값 
