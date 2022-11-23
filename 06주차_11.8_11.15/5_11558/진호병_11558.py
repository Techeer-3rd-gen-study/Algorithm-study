def dfs(start):
    for n in graph[start]:
        if visited[n] == 0:
            visited[n] = visited[start]+1
            dfs(n)
            
for _ in range(int(input())):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        v = int(input())
        graph[i].append(v)
    visited = [0]*(N+1)
    dfs(1)
    if(visited[N] > 0):
        print(visited[N])
    else:
        print(0)
   # print(visited[N] if visited[N] > 0 else 0)

# circle = int(input())



# for _ in range(circle):
#     N = int(input())
#     graph = [0 for _ in range(N+1)]
#     for i in range(1,N+1):
#         graph[i] = int(input())
#     start = graph[1]
#     count = 1
#     while (start != N and count <= N):
#         start = graph[start]
#         count += 1 
#     if(count > N) :
#         count =0
#     print(count)


