# The Game of Death

def dfs(v):
    for n in graph[v]:
        if check[n] == 0:
            check[n] = check[v]+1
            dfs(n)
            
for _ in range(int(input())):
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        v = int(input())
        graph[i].append(v)
    check = [0] * (N + 1)
    dfs(1)
    print(check[N] if check[N] > 0 else 0)