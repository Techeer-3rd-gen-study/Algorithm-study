# 16173번 : 점프왕 젤리
# BFS 풀이 

from collections import deque
import sys
input = sys.stdin.readline


def bfs(y, x):
    queue = deque()
    queue.append((y, x, graph[y][x]))
    
    while queue :
        y, x, d = queue.popleft()

        for i, j in [(1, 0), (0, 1)]:

            Y, X = y + d * i, x + d * j

            if 0 <= Y < n and 0 <= X < n and d != 0:
                if Y == X == n - 1:
                    return True
                queue.append((Y, X, graph[Y][X]))
    return False
        
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]    

print("HaruHaru" if bfs(0, 0) else "Hing")
