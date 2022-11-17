# 인접 -> bfs 

r,c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(map(str, input())))

# .: 빈칸, S: 양, W: 늑대, D: 울타리
flag = True
for i in range(r):
    for j in range(c):
        if graph[i][j] == "W":
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            if i == r and j == c:
                break
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
            
                if nx <= 0 or nx > r or ny <= 0 or ny > c:
                    break
                if graph[nx][ny] == "S":
                    flag = False
                    break
        elif graph[i][j] == "S":
            continue
        elif graph[i][j] == ".":
            graph[i][j] = "D"

if flag == False:
    print(0)
elif flag == True:
    print(1)
    for i in graph:
        print("".join(i))