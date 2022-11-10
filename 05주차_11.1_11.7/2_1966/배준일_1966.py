# 프린터 큐

from collections import deque
import sys

testcase = int(input())

for _ in range(testcase):
    n, m = map(int, input().split()) # 문서의 개수 N, 몇번째로 인쇄되었는지 궁금한 문서 M (맨 왼쪽 = 0)
    queue = deque(list(map(int, sys.stdin.readline().split()))) # 문서 나열
    count = 0
    while queue:
        biggest = max(queue)  #현재의 최댓값이 가장 먼저 배출되므로 최댓값을 저장
        front = queue.popleft() # 큐의 front를 뽑았으므로
        m -= 1 # 내 위치가 한 칸 당겨진다.

        if biggest == front: # 뽑은 숫자가 제일 큰 숫자일 때
            count += 1 # max값 제거 -> count++
            if m < 0: # m이 0이라는 것은 뽑은 숫자가 내 숫자라는 뜻.
                print(count)
                break

        else:   # 뽑은 숫자가 제일 큰 숫자가 아니면
            queue.append(front) # 제일 뒤로 밀려나게 됨
            if m < 0 :  # 제일 앞에서 뽑히면
                m = len(queue) - 1 # 제일 뒤로 이동