#조건 1: 로봇은 한 번에 오른쪽에 인접한 칸 또는 아래에 인접한 칸으로만 이동할 수 있다. 
#조건 2: 격자에 ○로 표시된 칸이 있는 경우엔 로봇은 그 칸을 반드시 지나가야 한다. 

# 입력의 첫째 줄에는 격자의 행의 수와 열의 수를 나타내는 두 정수 N과 M(1 ≤ N, M ≤ 15), 
# ○로 표시된 칸의 번호를 나타내는 정수 K(K=0 또는 1 < K < N×M)가 차례로 주어지며, 각 값은 공백으로 구분된다. 
# K의 값이 0인 경우도 있는데, 이는 ○로 표시된 칸이 없음을 의미한다. N과 M이 동시에 1인 경우는 없다.

# -> 최단경로찾는 확통 문제와 유사하게 풀이. (x+1, y) + (x, y+1)

n, m, k = [int(x) for x in input().split()]

def sol(y,x) :
    dp = [ [0 for _ in range(x+1)] for _ in range(y+1) ]

    for i in range(1, y+1):
        for j in range(1, x+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[y][x]


if k == 0:
    print(sol(n,m))
elif k != 0:
    n1 = (k-1) // m + 1
    m1 = k - ((n1-1) * m)
    case1 = sol(n1, m1)

    n2 = n - (n1-1)
    m2 = m - (m1-1)
    case2 = sol(n2, m2)

    print(case1 * case2)

    