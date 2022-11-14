# 백준 11725번 : 트리의 부모 찾기 

# BFS 메소드 --> 시간 초과 --> sys 로 해결 ! 
import sys
from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v]=True 
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력 
        p = queue.popleft()
        # 해당 원소와 연결된 노드 중에서 방문 하지않은 원소 큐에 삽입, 부모 리스트에 저장 
        for i in graph[p]:
            if not visited[i]:    # 방문 하지 않은 노드의 경우 
                parent[i] = p     # 부모 저장
                queue.append(i) 
                visited[i] = True  


n = int(sys.stdin.readline())
visited = [False] * (n + 1)
graph  = [[] for _ in range(n + 1)]

# 부모 노드 저장해둘 리스트
parent = [0] * (n + 1) 

# 그래프 입력 받기 
for i in range(n - 1):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)  
    graph[b].append(a)


bfs(graph, 1, visited)

# 두번째 노드부터 부모 노드 번호 출력
for i in range(2, n + 1): 
    print(parent[i])

