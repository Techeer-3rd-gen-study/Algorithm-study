# 11494 : 다이나믹이 뭐예요?
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

# dp 테이블 초기화
d = [[0] * (m + 1) for _ in range(n + 1)]
# 초기값 설정
d[0][0] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # d[i - 1][j] : ↓
        # d[i][j - 1] : →
        # d[i - 1][j - 1] : ↘
        d[i][j] = (d[i - 1][j] + d[i][j - 1] + d[i - 1][j - 1]) % 1000000007

print(d[n][m])