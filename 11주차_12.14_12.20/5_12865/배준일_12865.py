# 평범한 배낭
# https://hongcoding.tistory.com/50

n, k = map(int, input().split()) # 물품 수, 준서가 버틸 수 있는 무게
thing = [[0, 0]]

for _ in range(n):
    thing.append(list(map(int, input().split())))

dp = [[0] * (k + 1) for _ in range(n + 1)] # n번째 물건 까지 살펴보았을 때, 무게가 k인 배낭의 최대 가치 

for i in range(1, n + 1): # i = 담을 물건의 인덱스
    for j in range(1, k + 1): # j = 현재 가방 허용 무게
        w = thing[i][0] # 담을 물건의 무게
        v = thing[i][1] # 담을 물건의 가치

        if j < w: # 배낭에 담을 수 있을 경우
            dp[i][j] = dp[i - 1][j]
        else: # 배낭에 담을 수 없을 때 그 전꺼를 버리던가 or 현재 물건을 담지 않던가 중 최대치를 선택
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])