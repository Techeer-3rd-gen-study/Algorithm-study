#백준 1260번 : DFS 와 BFS

from collections import deque

# DFS 메서드 정의
def dfs(v) : 
    visit_dfs[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드 재귀적 방문 
    for i in range(1, n+1):
        if not visit_dfs[i] and graph[v][i] == 1:
            dfs(i)

# BFS 메서드 정의
def bfs(v) :
    queue = deque([v])
    visit_bfs[v] = True  

    # 큐가 빌 때까지 
    while queue :           
        # 큐에서 하나의 원소 뽑아 출력 
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 원소 큐에 삽입 
        for i in range(1, n+1):
            if not visit_bfs[i] and graph[v][i] == 1:
                queue.append(i)
                visit_bfs[i] = True


# 정점 개수, 간선 개수, 탐색 시작점 
n, m, v = map(int,input().split())

# 방문 체크
visit_dfs = [False] * (n+1)
visit_bfs = [False] * (n+1) 
graph = [[0]*(n+1) for i in range(n+1)]

# 노드 연결 -> 인접 리스트 
for _ in range(m) : 
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


dfs(v)
print()
bfs(v)