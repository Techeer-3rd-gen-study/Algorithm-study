from collections import deque

n = int(input())
stone = list(map(int, input().split()))
start = int(input()) - 1

visited = [0] * n
result = 0

def bfs(start):
    global result

    queue = deque()
    queue.append(start)
    visited[start] = 1
    result += 1

    while queue:
        idx = queue.popleft()
        for i in [-stone[idx], stone[idx]]:
            tmp = idx + i
            if 0 > tmp or tmp > n :
                pass
            elif 0 <= tmp < n and visited[tmp] == 0:
                queue.append(tmp)
                result += 1
                visited[tmp] = 1    
    return result

print(bfs(start))