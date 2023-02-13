# 11437.py
# https://www.acmicpc.net/problem/11437

n = int(input())

visited = [0] * (n+1)

graph = [ [] for _ in range(n+1) ]

for _ in range(n-1) :
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v, depth):
    visited[v] = True
    
    

m = int(input())
for _ in range(m) :
    x, y = map(int, input().split())

    
