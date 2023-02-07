# 11726 : 2xn 타일링

import sys
input = sys.stdin.readline

n = int(input())

# dp 테이블 초기화
d = [0] * 1001

d[1] = 1        # 2x1 타일 채우는 방법 1가지
d[2] = 2        # 2x2 타일 채우는 방법 2가지

for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2]) % 10007

print(d[n])