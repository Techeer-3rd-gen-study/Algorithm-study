def solution(n, computers):
    answer = 0
    visited = [False] * (n)
    
    
    def dfs(current):
        visited[current] = True

        for i in range(n):
            if not visited[i] and computers[current][i]:
                dfs(i)
                
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    
    return answer