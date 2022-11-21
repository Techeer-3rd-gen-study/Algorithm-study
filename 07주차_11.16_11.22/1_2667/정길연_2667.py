# 주변에 1이 있으면 인덱스 큐에 넣고 더이상 넣을게 없을 때 숫자로 초기화
# 큐의 크기 -> house num
# 탐색했던 곳 visited에 넣어놓고 탐색안한곳 중에서 위에 과정 반복 
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

graph = [list(input().rstrip()) for _ in range(n)]
house = list()      # 단지 내 집 수를 담는 list

def bfs(a, b, graph):
    house_num = -1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append((a, b))

    # 한 번 while 돌때 한 마을 순회
    while q:
        x, y = q.popleft()
        house_num += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n):
                if graph[nx][ny] == '1':
                    graph[nx][ny] = '0'
                    q.append((nx,ny))               
                elif graph[nx][ny] == '0':
                    pass
            else:
                pass

    return house_num

# print(all(1 in i for i in graph)) : True
while True :
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '1':
                house.append(bfs(i,j, graph))    
    if all('1' not in i for i in graph):
        break

house.sort()
for i in house:
    print(i)