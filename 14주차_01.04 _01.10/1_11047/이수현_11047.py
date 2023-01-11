# 11047 : 동전 0

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = 0

# 내림차순 정렬
coins.sort(reverse = True)

for i in coins:
    # 동전 개수
    count = count + k // i
    # 남은 거스름돈
    k = k % i
    # 더 이상 거스를 돈이 없을 경우 중지
    if k == 0:
        break

print(count)