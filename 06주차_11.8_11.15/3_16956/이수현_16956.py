# 16945 : 늑대와 양

import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input().rstrip()) for i in range(r)]

check = False

for i in range(r):
    for j in range(c):
        # 늑대 발견
        if graph[i][j] == 'W':
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            # 상하좌우 체크
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                # 양이 늑대와 마주칠 수 밖에 없다면
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 'S':
                    check = True
                    break
        # 양 발견            
        elif graph[i][j] == 'S':
            continue
        
        # 빈칸일 경우
        elif graph[i][j] == '.':
            graph[i][j] = 'D'

if check == True:
    print(0)

else:
    print(1)
    for i in graph:
        print(''.join(i))