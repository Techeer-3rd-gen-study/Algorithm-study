# 점프 점프

n = int(input()) # 돌다리의 돌 개수
stone = [0] + list(map(int, input().split())) # 돌 // 1번부터 시작
s = int(input()) # 출발점
visited = [False] * (n+1) # 1번부터 시작
cnt = 1 # 출발돌 count = 1

def dfs(x):
    global cnt
    
    for i in range(2):
        Ai = stone[x] # 점프 거리

        if i == 0:
            move = x + Ai # 오른쪽 이동
        else:
            move = x - Ai # 왼쪽 이동

        if move < 1 or move > n: # 예외처리
            continue
        
        if not visited[move]: # 돌 방문하지 않았다면
            visited[move] = True # 방문 표시
            cnt += 1
            dfs(move)
            
dfs(s)
print(cnt)
