from collections import deque

def dfs(start, visited=[]):  # 시작점, 방문 여부 확인 배열(dfs 재귀 될 동안 visited가 공유되어야하기 때문에)
    visited.append(start) # 일단 들어온 노드 방문 체크
    print(start, end=" ") 

    for adj in range(1,N+1): 
        if graph[start][adj] == 1 and adj not in visited: # 연결되어있지만 아직 방문하지않은 것이라면 
            dfs(adj, visited) # 다시 그 노드부터 dfs 재시작 즉, 파고 들어가면서 그 노드 출력하면 dfs 

def bfs(start):
    visited = [start]
    queue = deque()
    queue.append(start) # 스택에 방문한거 쌓기 (초기 시작점 세팅)

    while queue : # 큐가 비어있을 때까지 돌리는데 
        popThing = queue.popleft() # 스택에 첫번째 쌓인거 출력(즉 방문노드)
        print(popThing, end=" ")

        for adj in range(1, N+1): 
            if graph[popThing][adj] == 1 and adj not in visited: # 방문노드와 연결되어있지만 방문 안했으면
                visited.append(adj) # 그 노드 방문 처리하고
                queue.append(adj) # 스택에 추가 즉, 재귀가 아니라 그 방문노드와 연결된것 부터 싹다 검사하고 그 후에 쌓은 스택 이어서 출력
        

N,M,start = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)] # 이차원 배열로 연결노드 파악 

for _ in range(M):
    idx1, idx2 = map(int, input().split())
    graph[idx1][idx2] = graph[idx2][idx1] = 1 # 양방향 연결을 위한 것 


dfs(start)
print()
bfs(start)



