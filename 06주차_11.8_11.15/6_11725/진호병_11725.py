import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def dfs(start) : 
    global ans
    visited[start] = True
    for e in adj[start]: # adj[v]의 배열 요소 ex.adj[2] = [1,5] / e = 1이랑 e = 5 두개 실행 
        if not visited[e] : # 1은 방금 true로 됏으니 패스 5 아직 안했으니 ㄱ ㄱ
            ans[e] = start
            dfs(e)
         

n = int(input())

adj = [[] for _ in range(n + 1)]

ans = [0] * (n+1)

visited = [False] * (n+1)

for i in range(n-1) :
    x,y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
    

dfs(1)

for i in range(2,n+1) :
    print(ans[i])
