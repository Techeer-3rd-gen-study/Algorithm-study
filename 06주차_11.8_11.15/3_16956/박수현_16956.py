import sys

r, c = map(int, sys.stdin.readline().split())

# 2차원 리스트의 맵 정보 입력 받는다.
graph = []
for _ in range(r):
    graph.append(list(map(str, input())))

# 좌/우/위/아래 방향 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 늑내가 양이 있는 칸으로 갈 수 있으면 True,
# 아니라면 False
boolean = False

# 2차원 리스트를 양이 있는 곳 좌/우/위/아래에 늑대가 있는지 확인
for i in range(r):
    for j in range(c):
        if graph[i][j] == "W":
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]

                # 2차원 리스트 범위를 벗어나면 넘긴다.
                if x <= -1 or x >= r or y <= -1 or y >= c:
                    continue

                # 늑대가 있으면 반복문을 멈추고 0을 출력
                if graph[x][y] == "S":
                    boolean = True
                    break

if boolean:
    print(0)
else:
    print(1)
    # 늑대와 양이 있는 위치를 제외하고 모두 울타리 설치
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                graph[i][j] = "D"
    for k in graph:
        print(''.join(k))