# 네트워크

from collections import deque
def solution(n, computers):
    visited = [0 for _ in range(n)]
    answer = 0
    
    def bfs(start):
        visited[start] = True
        q = deque([(start)])
        
        while q:
            now = q.popleft()
            visited[now] = True
            
            for i in range(len(computers[now])):
                if not visited[i] and computers[now][i]:
                    q.append(i)
    
    for i in range(n):
        if not visited[i]: # visited가 False만 체크
            bfs(i) # bfs로 연결된 네트워크 체크
            answer += 1
                    
    return answer