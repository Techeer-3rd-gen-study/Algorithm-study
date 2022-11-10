# 카드 2

import sys
from  collections import deque

n = int(sys.stdin.readline())

q = deque()

# 카드 생성
for i in range(1, n + 1):
    q.append(i)

while len(q) != 1:
    # 맨 위 카드(왼쪽) 버리기
    q.popleft()
    # 카드 맨 뒤로(오른쪽) 옮기기
    q.append(q.popleft())

print(q[0])