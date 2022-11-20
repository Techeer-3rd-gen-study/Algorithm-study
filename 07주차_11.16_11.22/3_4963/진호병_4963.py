from collections import deque

def bfs(sx,sy) :  # 전 문제는 4개 검사 이 문제는 8개 검사
    ax = [0, 0, -1, -1, -1, 1, 1, 1]
    ay = [1, -1, 1, 0, -1, 1, 0, -1]
    queue = deque()


    queue.append([sx,sy])

    while queue:

        x,y = queue.popleft()
        board[x][y] = 0
        for i in range(8):
            X = x + ax[i]
            Y = y + ay[i]
            if  (0<= X < w) and (0<= Y < h) and board[X][Y] == 1 : 
                queue.append([X,Y])
                board[X][Y] = 0 


while True:
    h,w = map(int, input().split()) 

    if(h == 0 and w == 0):
        break

    else : 
        board = []
        island = 0
        for _ in range(w):
            board.append(list(map(int,input().split(' '))))

        for i in range(w): 
            for j in range(h): 
                if board[i][j] == 1: 
                    bfs(i,j)
                    island += 1 
        
        print(island)



