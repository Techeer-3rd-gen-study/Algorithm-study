# 백준 2606번 : 바이러스

n = int(input())
m = int(input())
graph = [[0]*(n+1) for i in range(n+1)]

# 노드 연결 -> 인접 리스트 
for _ in range(m) : 
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [False] * (n+1)

# DFS 풀이 
def dfs(v) : 
    visited[v] = True
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


dfs (1)
print(sum(visited)-1)


'''
# BFS 풀이 
from collections import deque
def bfs(v) :
    queue = deque([v])
    visited[v] = True  

    while queue :           
        v = queue.popleft()
        for i in range(1, n+1):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True

bfs (1)
'''
