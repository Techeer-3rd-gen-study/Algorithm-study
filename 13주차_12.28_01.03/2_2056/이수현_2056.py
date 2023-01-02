# 2056 : 작업
# https://haesoo9410.tistory.com/220

import sys
input = sys.stdin.readline

n = int(input())
# dp 테이블 초기화
dp = [0] * (n + 1)

for i in range(1, n + 1):
    # 작업 번호 입력받기
    lst = list(map(int, input().split()))
    # 각 작업에 선행관계에 있는 작업들 중 
    # 가장 늦게 끝나는 것에서 현재 작업이 걸리는 시간을 더하면 현재 작업이 끝나는 시간
    for num in lst[1 : ]:
        dp[i] = max(dp[i], dp[num] + lst[0])

print(max(dp))