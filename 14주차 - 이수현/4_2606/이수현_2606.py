# 2606 : 바이러스

from collections import deque

n = int(input())
connect = int(input())
graph = [[] for i in range(n + 1)]  # n개의 컴퓨터 연결 
visited = [False] * (n + 1)         # 방문 확인용 리스트
cnt = 0                             # 웜 바이러스에 걸리게 되는 컴퓨터 수

for i in range(connect):
    a, b = map(int, input().split())
    # 양방향 처리
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, v):
    global cnt
    queue = deque([v])
    # 큐에 값이 없을 때까지
    while queue:
        # 첫 번째 요소부터 pop하고 체크
        pop = queue.popleft()
        visited[pop] = True
        
        for i in graph[pop]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                cnt += 1
    print(cnt)

bfs(graph, 1)