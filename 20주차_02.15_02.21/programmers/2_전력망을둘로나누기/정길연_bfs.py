from collections import deque

def solution(n, wires):
    graph = [ [] for _ in range(n+1) ]
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        q = deque()
        visited = [False] * (n+1)
        q.append(start)
        cnt = 0
        while q:
            node = q.popleft()
            visited[node] = True
            for i in graph[node]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    cnt += 1
        return cnt 
    
    result = 1e9
    # 하나씩 끊어보면서 bfs 돌리기
    for wire in wires:
        a, b = wire
        graph[a].remove(b)
        graph[b].remove(a)
        
        # 끊으면 해당 간선으로 연결된 각 노드가 부모가 되므로
        result = min( abs( bfs(a) - bfs(b)), result )
        
        # 다시 붙이기
        graph[a].append(b)
        graph[b].append(a)
        
    return result