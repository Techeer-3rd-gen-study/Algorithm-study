from collections import deque

def bfs(sx,sy) : 
    cntVillage = 1
    queue = deque()
    queue.append([sx,sy])
    visited[sx][sy] = 1

    while queue:
        ax = [0,0,-1,1]
        ay = [-1,1,0,0]
        x,y = queue.popleft()
        for i in range(4):
            X = x + ax[i]
            Y = y + ay[i]
            # 근처 방문처가 범위 밖이 아니고 , 방문이 아직 안됐으며, 집이 있으면
            if  (0<= X < N) and (0<= Y < N) and board[X][Y] == 1 and visited[X][Y] != 1 :
                cntVillage += 1 
                visited[X][Y] = 1
                queue.append([X,Y])

    village.append(cntVillage) # queue를 다 돌고 나서의 한 단지의 수 
           



N = int(input())
visited = [[0 for _ in range(N)] for _ in range(N)] # 방문체크
village = [] # 단지 배열
board = [] # 지도

for i in range(N):
    board.append(list(map(int,input())))

for i in range(N): # board를 방문하면서 집이 있으면 bfs 실행
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] != 1 : 
            bfs(i,j)

village.sort()

print(len(village))
print(*village, sep="\n") # 배열 요소 여러번 반복 출력