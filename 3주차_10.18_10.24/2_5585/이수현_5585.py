# 거스름돈

import sys

money = int(sys.stdin.readline())
count = 0
# 거스름돈 계산
change = 1000 - money

# 가장 큰 단위부터 확인
coin = [500, 100, 50, 10, 5, 1]

for i in coin:
    # 동전 개수 계산
    count = count + change // i
    # 남은 거스름돈
    change = change % i
    # 더 이상 거스를 돈이 없을 경우 중지
    if change == 0:
        break

print(count)