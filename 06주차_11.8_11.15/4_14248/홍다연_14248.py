# 백준 14248번 : 점프 점프 

from collections import deque

# BFS 메서드
def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        v = queue.popleft()
        for move in [- graph[v], graph[v]]:  # 왼쪽, 오른쪽
            newV = v + move
            if (0 <= newV < n) and visited[newV] == False:   # 돌 다리 안에서, 가보지않은 곳이면 큐에 추가하고, 방문 체크를 해준다. 
                queue.append(newV)
                visited[newV] = True


n = int(input())   # 돌다리 돌 개수 
graph = list(map(int, input().split()))  # 돌 번호 
s = int(input()) - 1   # 시작 위치

# 방문 정보 체크 
visited = [False] * (n)

bfs(s)
print(sum(visited))

