# 늑대와 양

import sys
input=sys.stdin.readline

R, C = map(int, input().split()) # 목장의 크기

board = [list(input().rstrip()) for _ in range(R)] # 목장

sign = False # 늑대가 양한테 갈 수 있는지

for i in range(R) :
    for j in range(C) :
        # 늑대일 경우
        if board[i][j] == "W" :
            dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
            dy = [0, 0, -1, 1]  # 상, 하, 좌, 우

            for k in range(4) :
                nx = i + dx[k]
                ny = j + dy[k]

                if 0<=nx<R and 0<=ny<C and board[nx][ny]=="S":
                        sign = True
                        break
        # 양일 경우
        elif board[i][j] == "S" :
            continue

        # 빈칸일 경우
        elif board[i][j] == "." :
            board[i][j] = "D"

if sign :
    print(0)

else :
    print(1)
    for i in board :
        print(''.join(i))

