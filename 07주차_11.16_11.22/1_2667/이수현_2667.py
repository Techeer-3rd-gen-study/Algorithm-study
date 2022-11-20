# 2667 : 단지 번호 붙이기

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

# dfs로 특정한 노드를 방문한 뒤 연결된 노드 방문
def dfs(x, y):
    global count
    # 지도를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 1:
        # 단지 수 세기
        count += 1
        # 해당 노드 방문처리
        graph[x][y] = 0
        # 상하좌우 위치 모두 재귀적 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
count = 0
count_house = []

for i in range(n):
    for j in range(n):
        # 집이 있는 곳이라면
        if dfs(i, j) == True:
            # 단지에 속해있는 집의 개수 추가
            count_house.append(count)
            # 단지 수 추가
            result += 1
            # 초기화
            count = 0

count_house.sort()

print(result)
for i in count_house:
    print(i)
