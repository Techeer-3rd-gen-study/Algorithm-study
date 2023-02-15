from collections import deque


def bfs(current, tired, dungeons):
    queue = deque()
    queue.append([current, tired, 0, [False for _ in range(len(dungeons))]])
    counted = []
    while queue:
        current, tired, count, visited = queue.popleft()
        visited[current] = True
        count += 1
        tired -= dungeons[current][1]
        counted.append(count)
        
        for i in range(len(dungeons)):
            if not visited[i] and tired >= dungeons[i][0]:
                queue.append([i, tired, count, visited[:]])  
                
    return max(counted)
            
    
def solution(k, dungeons):
    answer = -1
    
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k :
            answer = max(answer ,bfs(i, k, dungeons) )

    return answer