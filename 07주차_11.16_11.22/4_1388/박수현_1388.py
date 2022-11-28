# dfs 알고리즘 함수 정의
def dfs(x,y):
    # 바닥 장식 모양이 '-' 일 때
    if graph[x][y] == '-':
        graph[x][y] = 1	    # 해당 노드 방문처리
        for _y in [1,-1]:   # 양옆(좌우) 확인하기
            Y = y + _y
            # 좌우 노드가 주어진 범위를 벗어나지 않고 '-'모양이라면 재귀함수 호출
            if (Y > 0 and Y < m) and graph[x][Y] == '-':
                dfs(x,Y)

    # 바닥 장식 모양이 '|' 일 때
    if graph[x][y] == '|':
        graph[x][y] = 1	    # 해당 노드 방문처리
        for _x in [1,-1]:   # 상하(위아래) 확인하기
            X = x + _x  
            # 상하 노드가 주어진 범위를 벗어나지 않고 '|' 모양이라면 재귀함수 호출
            if (X > 0 and X < n) and graph[X][y] == '|':
                dfs(X,y)

n,m = map(int, input().split()) # 방 바닥의 세로 크기 n, 가로 크기 m
graph = []  # 2차원 리스트의 맵 정보 저장할 공간
for _ in range(n):
    graph.append(list(input()))

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i,j)    # 노드가 '-'이나 '|'일 경우에 재귀함수 호출
            # dfs 처리를 통해 방문한 노드는 1로 변경되므로, 방문하지 않은 노드에 대해서만 체크할 수 있음
            count += 1
            # 재귀 호출을 통해 가로 혹은 세로로 동일한지 확인할 수 있기 때문에 몇 개의 판자를 사용했는지 확인하기 위해서는 함수 호출이 끝난 후 +1일 해주는 작업만 남게됨
 
print(count)
