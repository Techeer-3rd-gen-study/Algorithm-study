from collections import deque

com = int(input())    # 컴퓨터 개수
link = int(input())    # 간선 개수
virused = 0         # 바이러스에 걸린 컴퓨터 개수

# 그래프 초기화
graph = [ [0] * (com+1) for _ in range(com+1) ]
for _ in range(1, link+1) :
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [False] * (com+1)

def dfs(start) :
    global virused
    visited[start] = True

    for i in range(1, com+1):
        if graph[start][i] == 1 and visited[i] == False:
            dfs(i)
            virused += 1

def bfs(start):
    global virused

    q = deque()
    q.append(start)
    visited[start] = True
        
    while q :
        now = q.popleft()
        

        for i in range(1, com+1) :
            if graph[now][i] == 1  and visited[i] == False:
                q.append(i)      
                visited[i] = True 
                virused += 1

    return print(virused)
                
                
dfs(1)
print(virused)
    
