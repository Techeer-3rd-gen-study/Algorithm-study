# 9084 : 동전

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().rstrip().split()))
    m = int(input())

    # dp 테이블 초기화
    d = [0] * (m + 1)
    # 0원은 어느 동전으로든지 만들 수 있으므로
    d[0] = 1

    for coin in coins:
        for i in range(m + 1):
            # 만드려는 돈이 가지고 있는 화페단위보다 크거나 같을 경우
            # 이전 경우의 수에 현재 동전으로 만들 수 있는 경우의 수 더하기
            if i >= coin:
                d[i] += d[i - coin]
    
    print(d[m])