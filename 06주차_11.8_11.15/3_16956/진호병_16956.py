from collections import deque

R, C = map(int, input().split())

graph = [list(input()) for _ in range(R)]

Defence = 0

def bfs(x,y) : 
    ox = [0,0,-1,1]
    oy = [-1,1,0,0]
    global Defence

    for i in range(4):
        X = x + ox[i]
        Y = y + oy[i]

        if (0<=X<R) and (0<=Y<C) and graph[X][Y] == "." :
            graph[X][Y] = 'D'
        elif (0<=X<R) and (0<=Y<C) and graph[X][Y] == "W" :
            Defence = 1
            break

for i in range(R) : 
    for j in range(C) : 
        if graph[i][j] == "S":
            bfs(i,j)

if Defence == 1 : 
    print(0)
else : 
    print(1)
    for i in range(R):
        for j in range(C):
            print(graph[i][j],end="")
        print("")