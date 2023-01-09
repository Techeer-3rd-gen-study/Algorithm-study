# 1966 : 프린터 큐

import sys
from collections import deque

input = sys.stdin.readline

case = int(input())

for _ in range(case):
    n, target = map(int, input().split())
    q = deque(list(map(int, input().split())))
    idx = deque(list(range(n)))
    count = 0

    # q가 비어있을 때까지 실행
    while q:
        # 첫번째 원소가 중요도가 가장 크면
        if q[0] == max(q):
            count += 1
            # 인쇄(삭제)
            q.popleft()
            # 인덱스 추출
            pop_idx = idx.popleft()

            # 우리가 찾는 문서라면
            if pop_idx == target:
                print(count)
        # 첫번째 원소의 중요도가 가장 크지 않을 경우
        else:
            # 중요도 순으로 출력하기 위해 뒤로 보내기
            q.append(q.popleft())
            idx.append(idx.popleft())

