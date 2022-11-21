# 목장의 가로y, 세로x
y, x = map(int, input().split())

# for i in range(x) :
#     graph = list(map(input().split()))
graph = [list(input()) for _ in range(y)]

# . 빈칸 S 양 W 늑대
# graph 전체 탐색

# 늑대가 양한테 못가면 True
flag = True

for i in range(y):
    for j in range(x):   
        if graph[i][j] == 'S':
            pass  
        elif graph[i][j] == 'W':    # 늑대일 경우 상하좌우에 S가 있는 지 확인한다
            # 상하좌우 확인
            for k in range(4) :
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]
                nx = j + dx[k]
                ny = i + dy[k]
                if ( (0 <= nx < x) and (0 <= ny < y) ):     
                    if(graph[ny][nx] == 'S') :    # 상하좌우안에 양이 있을 때
                        flag = False
                        break
                    elif(graph[ny][nx] == '.') :
                        graph[ny][nx] = 'D' 
        elif graph[i][j] == '.':      
            pass


if flag == True :
    print(1)
    for i in range(y):
        for j in range(x):
            print(graph[i][j],end="")
        print()
else : 
    print(0)




        


