# 점프 점프

from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
stone = list(map(int, input().rstrip().split()))
start = int(input().rstrip()) - 1

visited = [False] * n
cnt = 0

def bfs(v):
    global cnt
    q = deque([v])
    visited[v] = True
    cnt += 1

    while q:
        now = q.popleft()
        
        for i in [-stone[now], stone[now]]:
            search = i + now

            if search < 0 or search > n:
                pass
            elif 0 <= search < n and visited[search] == False:
                q.append(search)
                cnt += 1
                visited[search] = True
                
    return cnt

print(bfs(start))


