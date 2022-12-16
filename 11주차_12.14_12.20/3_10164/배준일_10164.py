# 격자상의 경로

# 오른쪽 or 아래
# O 표시 반드시 지나야함
# k = 0이면 동그라미 표시된게 없다.
import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
grid_list = []
x, y = 0, 0 # k일 때 좌표 저장용 변수

for i in range(0, n):
    # grid_list에 n * m만큼 값 2차원 리스트로 저장 
    lst = []

    for j in range(1, m + 1):
        lst.append(i * m + j)

    grid_list.append(lst)

dp[1][0] = 1
dp[1][1] = 1


if k == 0:
    # 1~(n, m)까지 가는 dp
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    print(dp[n][m])

else:
    is_k = 0 # k인지 판별하는 flag
    until_k = 0 # 1~k까지의 경로값 저장

    # 1~k까지 가는 dp
    for i in range(1, n + 1):
        if is_k == 1: # 이중 for문 break 
            break
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

            if grid_list[i - 1][j - 1] == k:
                x, y = i, j # k일 때 좌표 저장
                is_k = 1 
                until_k = dp[i][j] # 1~k값일 때 경로값 저장
                dp = [[0] * (m + 1) for _ in range(n + 1)] # dp 초기화
                break

    # k~(n, m)까지 가는 dp
    for i in range(x, n + 1):
        for j in range(y, m + 1):
            dp[x][y] = 1 # 초기값 설정
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # 두 값 곱하기
    print(dp[n][m] * until_k)
    