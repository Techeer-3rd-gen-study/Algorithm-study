# 답지 참고
n,m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(input()))
count= 0
for i in range(n):
    pre = "/"
    for j in range(m):
        if board[i][j] =='-':
            if board[i][j] != pre : count += 1
        pre = board[i][j]

for j in range(m):
    if board[i][j] == '|':
        if board[i][j] != pre: count+=1
    pre = board[i][j]
print(count)

