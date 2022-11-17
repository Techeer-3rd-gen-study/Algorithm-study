import sys

input = sys.stdin.readline

def dfs(node):
    for i in graph[node]:
        if check[i] == 0:
            check[i] = check[node] + 1
            dfs(i)

for i in range(int(input())):
    length = int(input())
    graph = [[] for _ in range(length+1)]
    check = [0]*(length+1)
    for i in range(1, length+1):
        graph[i].append(int(input()))
    dfs(1)
    print(check[length])
