def dfs(x, y):
    # 주어진 정사각형 크기보다 더 커지는 경우 return
    if x >= num or y >= num:
        return 
    # 이미 방문한 경우 return
    if visited[x][y] == True:
        return 
    # 도착한 경우 종료
    if graph[x][y] == -1:
        print('HaruHaru')
        exit() # 파이썬에서 코드 강제 종료하는 방법
    # 위 경우의 수가 모두 아닌 경우 방문 가능한 장소이므로, 방문한 장소임을 표시
    visited[x][y] = True
    # 오른쪽 한 번, 왼쪽 한 번 방문
    for i in range(2):
        # 반복문
            # 반복문 0번째 : dx=1, dy=0
                # x + dx[0] * graph[x][y] -> x + 1 * graph[x][y]
                    # 현재 위치 + 오른쪽으로 한 칸 이동 * 현재 위치의 값
                # y + dy[0] * graph[x][y] -> y + 0 * graph[x][y]
                    # 현재 위치
            # 반복문 1번째 : dx=0, dy=1
                # x + dx[1] * graph[x][y] -> x + 0 * graph[x][y]
                    # 현재 위치
                # y + dy[1] * graph[x][y] -> y + 1 * graph[x][y]
                    # 현재 위치 + 아래쪽으로 한 칸 이동 * 현재 위치의 값
        nx = x + dx[i] * graph[x][y]
        ny = y + dy[i] * graph[x][y]
        dfs(nx, ny)
    return True

num = int(input())
graph = []
for i in range(num):
    graph.append(list(map(int, input().split(" "))))    

visited = []
for _ in range(num):
    visited.append([False] * num)
 
dx = [1, 0]
dy = [0, 1]
 
if dfs(0, 0) == True:
    print('Hing')

