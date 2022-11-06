# 홍다연_예제4_1 : 상하좌우

n = int(input())
x, y = 1, 1
moves = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

move_lst = ["L","R","U","D"]

for m in moves :
    for i in range(len(move_lst)):
        if m == move_lst[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:  # 공간을 벗어날 때 
        continue

    x,y = nx, ny

print(x,y)        
