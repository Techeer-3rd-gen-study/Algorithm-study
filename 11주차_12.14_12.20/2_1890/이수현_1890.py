# 1890 : 점프

import sys
input = sys.stdin.readline

n = int(sys.stdin.readline())
game = [list(map(int, input().rstrip().split())) for _ in range(n)]

# dp 테이블
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1 

# 반복문을 통해 갈 수 있는 그래프의 좌표를 탐색
for i in range(n):
    for j in range(n):

        # 오른쪽 끝 점이면 중지
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break

        # 오른쪽으로 이동
        if j + game[i][j] < n:
            dp[i][j + game[i][j]] += dp[i][j]

        # 아래로 이동
        if i + game[i][j] < n:
            dp[i + game[i][j]][j] += dp[i][j]