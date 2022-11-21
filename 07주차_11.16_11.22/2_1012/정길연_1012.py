# 빈공간에 지렁이가 들어가는 줄알고 대체 왜 3마리가 아니라 5마리일까 머리터질뻔했던 문제 ..
# 1로 체킹돼있는 인접한 묶음 체킹 -> 한 번 돌때 0으로 초기화
from collections import deque

def bfs(b, a, graph) :
    q = deque()
    q.append((b,a))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q :
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<m and 0<=ny<n):
                if graph[ny][nx] == 1:
                    q.append((ny,nx))
                    graph[ny][nx] = 0
            else:
                pass
    return 


test_case = int(input())
while test_case :
    m, n, num = list(map(int, input().split()))   # 가로, 세로, 배추개수
    bug_cnt = 0

    graph= [ [0] * m for _ in range(n) ]  # (n,m)
    for _ in range(num):
        y, x = map(int, input().split()) # 가로, 세로로 입력받음 
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j, graph)
                bug_cnt += 1

    print(bug_cnt)
    test_case -= 1