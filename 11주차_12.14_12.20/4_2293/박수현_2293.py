# 도움을 받은 링크 주소입니다
# https://pacific-ocean.tistory.com/200
# https://mong9data.tistory.com/68

n, k = map(int, input().split())
c = []

dp = [0 for i in range(k + 1)]
dp[0] = 1

for i in range(n):
    c.append(int(input()))

for i in c:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])
