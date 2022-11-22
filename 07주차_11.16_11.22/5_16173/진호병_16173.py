import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

cx = [0, 1]
cy = [1, 0]

def dfs(ox,oy) : 
    global test
    jump = board[ox][oy]
    board[ox][oy] = 0

    if ox == N-1 and oy == N-1:
        test = True
        return

    for i in range(2):
        X = ox + cx[i]*jump
        Y = oy + cy[i]*jump

        if (0 <= X < N) and (0 <= Y < N) and board[X][Y] != 0: 
                dfs(X,Y)



N = int(input())

board = [[0] * (N) for _ in range(N)]

test = False

for i in range(N) : 
    lineArr = list(map(int, input().split()))
    for j in range(N) : 
        board[i][j] = lineArr[j]

dfs(0,0)

if not test : 
    print("Hing")
else : 
    print("HaruHaru")




