# 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 문제의 규칙에 맞게 갈 수 있는 경로의 개수를 출력
# -> 0을 안찾아도 되고, n-1 일때 완료

n = int(input())
game_map = [list(map(int, input().split())) for _ in range(n)]

dp = [ [0] * n for _ in range(n) ]  
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break
        else : 
            cnt = game_map[i][j]
            if j + cnt < n:
                dp[i][j + cnt] += dp[i][j]      # 오른쪽 이동
            if i + cnt < n:
                dp[i + cnt][j] += dp[i][j]      # 아래 이동