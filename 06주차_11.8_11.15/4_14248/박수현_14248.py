import sys
input = sys.stdin.readline # input함수 빠르게
sys.setrecursionlimit(10**6) # dfs 재귀호출 충분히늘려두기
n=int(input()) # 돌 개수
b=list(map(int, input().split())) # 각 돌다리별로 움직일 수 있는 칸의 개수
s=int(input()) # 출발점
cnt=1 # 방문한 돌 개수. 출발점 1개부터
v=[0]*n # 방문한 돌 표시
def dfs(x):
    global cnt
    for nx in (x+b[x], x-b[x]):
        if 0<=nx<n and v[nx]==0:
            cnt+=1;v[nx]=1
            dfs(nx)
dfs(s-1)
print(cnt)
