# 상수

import sys

a, b = map(int, sys.stdin.readline().split())

# 받은 세 자리 수를 역순으로 정렬
re_a = str(a)[::-1]
re_b = str(b)[::-1]

# 큰 수 출력
if re_a > re_b:
    print(re_a)
else:
    print(re_b)

