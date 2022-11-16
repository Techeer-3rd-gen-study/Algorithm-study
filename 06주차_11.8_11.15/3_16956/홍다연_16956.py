# 백준 16956번 : 늑대와 양 
# 늑대 사방으로 울타리를 치는 코드 방법은 예제는 다 맞는데 틀렸습니다가 떠서 빈공간을 모두 울타리로 변경하는 코드로 풀었습니다. 

r, c = map(int, input().split())

graphs = [list(input()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
success = True

# 양 옆에 늑대가 있을 경우 -> 0
for i in range(r):
    for j in range(c):
        if graphs[i][j] == 'S' :
            for k in range(4) :
                nx = i + dx[k]
                ny = j + dy[k]

                if -1 < nx < r and -1 < ny < c :    # 범위 내에서 확인 
                    if graphs[nx][ny] == 'W' : 
                        success = False                      
            

if not success : print(0)

else : 
    print(1)
    # '.' 을 모두 울타리로 변경하고 출력 
    for i in range(r):
        for j in range(c):
            if graphs[i][j] == '.' :    
                graphs[i][j] = 'D'

    for p in range(r):
        print(''.join(graphs[p]))



# 늑대 주변을 울타리로 치는 방법 . 
'''
else : 
    print(1)
    for i in range(r):
        for j in range(c):
            # 늑대가 나오면 주변을 다 울타리 치고, 출력 
            if graphs[i][j] == 'W' :
                for n in range(4) :
                    xx = i + dx[n]
                    yy = j + dy[n]

                    if -1 < xx < r and -1 < yy < c :
                        graphs[xx][yy] = 'D'

    for p in range(r):
        print(''.join(graphs[p]))
'''



# 알고리즘이 더 복잡해지는 것 같아 뺐습니다.
'''
# 목장에 양만 있는 경우, 또는 늑대만 있는 경우 
for graph in graphs :
    if 'S' not in graph or 'W' not in graph:
        print(1)
        for i in range(r):
            print(''.join(graphs[i]))
'''
