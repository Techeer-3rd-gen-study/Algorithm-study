# 8911번 : 거북이 

# 북 0, 동 1, 남 2, 서 3 
dx = (0, 1, 0, -1) 
dy = (1, 0, -1, 0)
# 방향  
dirL = (3, 0, 1, 2) 
dirR = (1, 2, 3, 0)

for _ in range(int(input())):  
    path = list(input().strip()) 
    
    # x축, y축, 방향 
    x, y, d = 0, 0, 0   
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
 
    for i in path:
        if i == "F":
            x += dx[d]
            y += dy[d]
        elif i == "B":
            x -= dx[d]
            y -= dy[d]

        elif i == "L":
            d = dirL[d]
        elif i == "R":
            d = dirR[d]
            

        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        
    print(abs(max_x - min_x) * abs(max_y - min_y))