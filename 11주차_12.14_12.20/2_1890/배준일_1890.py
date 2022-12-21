# 점프
# 현재 칸에 적혀있는 수 만큼 오른쪽이나 아래로만

import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 게임판의 크기
N_list = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1 # 초기값 지정

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1: # 목표 지점 도착
            print(dp[i][j])
            break
        
        move = N_list[i][j]

        if j + move < N: # 오른쪽 이동
            dp[i][j + move] += dp[i][j]
        
        if i + move < N: # 아래 이동
            dp[i + move][j] += dp[i][j]
        