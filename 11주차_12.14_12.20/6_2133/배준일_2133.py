# 타일 채우기 
# https://my-coding-notes.tistory.com/201

import sys
input = sys.stdin.readline

n = int(input().rstrip())
# n+1은 1이 입력될 경우 dp[2]가 인덱스를 초과하게 되므로 
# n+2로 충분히 크게 만들어주자.
dp = [0] * (n + 2)
dp[2] = 3

if n % 2 == 1: # 홀수일 때
    print(0)
else:
    for i in range(4, n + 1, 2):
        dp[i] += dp[i - 2] * 3 # 끝이 2칸

        for j in range(i - 4, 0, -2):
            dp[i] += dp[j] * 2 # 각 j마다 고유모양 * 뒤집은거
        
        dp[i] += 2 # 고유모양 +2
    
    print(dp[n])
