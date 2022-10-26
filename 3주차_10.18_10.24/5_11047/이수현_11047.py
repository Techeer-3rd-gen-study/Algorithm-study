# 동전 0

import sys

n, k = map(int, sys.stdin.readline().split())
money = []
count = 0

# 동전 입력받기
for _ in range(n):
    input = int(sys.stdin.readline())
    money.append(input)

# 내림차순 정렬
money.sort(reverse=True)

for i in money:
    # 동전 개수 계산
    count = count + k // i
    # 남은 거스름돈
    k = k % i
    # 더 이상 거스를 돈이 없을 경우 중지
    if k == 0:
        break

print(count)