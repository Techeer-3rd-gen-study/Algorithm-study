# 점프 점프

n = int(input()) # 돌다리의 돌 개수
stone = [0] + list(map(int, input().split())) # 돌 // 1번부터 시작
s = int(input()) # 출발점
visited = [False] * (n+1)
cnt = 1

def dfs(x):
    global cnt
    
    for i in range(2):
        Ai = stone[x] # 점프 거리
        
        if i == 0:
            move = x + Ai
        else:
            move = x - Ai

        if move < 1 or move > n:
            continue
        
        if not visited[move]:
            visited[move] = True
            cnt += 1
            dfs(move)
            
dfs(s)
print(cnt)