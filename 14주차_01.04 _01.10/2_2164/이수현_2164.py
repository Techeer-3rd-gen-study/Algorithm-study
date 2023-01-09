# 2164 : 카드2

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

q = deque()

# 카드 생성
for i in range(1, n + 1):
    q.append(i)

# 큐의 길이가 1일때까지
while len(q) != 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])