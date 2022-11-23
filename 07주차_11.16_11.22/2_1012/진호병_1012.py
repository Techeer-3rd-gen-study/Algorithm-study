from collections import deque
import sys
input = sys.stdin.readline

def bfs(sx,sy) : 
    ax = [0,0,-1,1]
    ay = [-1,1,0,0]
    queue = deque()

    queue.append([sx,sy])

    while queue:

        x,y = queue.popleft()
        
        for i in range(4):
            X = x + ax[i]
            Y = y + ay[i]

            # 근처 방문처가 범위 밖이 아니고 , 방문이 아직 안됐으며, 집이 있으면
            if  (0<= X < N) and (0<= Y < M) and farm[X][Y] == 1 : 
                queue.append([X,Y])
                farm[X][Y] = 0 #????? 이거 때문에 시간 초과 난다 이유 모르겠음



           
total = int(input())


for _ in range(total) :
    M,N,K = map(int, input().split())
    groupCnt = 0
    farm = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x,y = map(int, input().split())
        farm[y][x] = 1 

    for i in range(M): 
        for j in range(N):
            if farm[j][i] == 1:
                bfs(j,i)
                groupCnt += 1 
    print(groupCnt)