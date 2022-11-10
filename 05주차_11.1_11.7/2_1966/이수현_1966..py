# 프린터 큐

import sys
from  collections import deque

input = sys.stdin.readline

case = int(input())

for _ in range(case):
    n, target = map(int, input().split())
    q = deque(list(map(int, input().split())))
    idx = deque(list(range(n)))         # 문서의 인덱스 담을 큐 생성
    count = 0

    while q:
        # 맨 앞의 원소의 중요도가 가장 크다면 
        if q[0] == max(q):
            count += 1
            # 중요도 가장 큰 원소 삭제
            q.popleft()
            # 중요도 가장 큰 원소의 인덱스 추출
            pop_idx = idx.popleft()

            # 우리가 찾는 문서라면 인쇄순서 출력
            if pop_idx == target:
                print(count)

        # 맨 앞의 원소 맨 뒤로 보내기
        else:
            q.append(q.popleft())
            idx.append(idx.popleft())